#!/usr/bin/env python3
"""Build gate untuk portfolio statis: cek referensi, id ganda, alt/lazy, JSON-LD, sitemap.
Pakai: python3 scripts/check.py   (exit 0 = lolos, 1 = ada masalah)
"""
import json
import pathlib
import re
import subprocess
import sys
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent.parent
ERRORS: list[str] = []
WARN: list[str] = []

SKIP_TAGS = {"br", "img", "input", "meta", "link", "hr", "source", "area", "base", "col", "embed", "param", "track", "wbr"}


class Scan(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.refs: list[str] = []
        self.imgs: list[dict] = []
        self.ldjson: list[str] = []
        self._in_ld = False
        self._buf: list[str] = []
        self.stack: list[str] = []
        self.unbalanced: list[str] = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.append(a["id"])
        for key in ("src", "href"):
            v = a.get(key)
            if v and not re.match(r"^(https?:|mailto:|tel:|#|data:|/|javascript:)", v):
                self.refs.append(v.split("?")[0])
        if tag == "img":
            self.imgs.append(a)
        if tag == "script" and a.get("type") == "application/ld+json":
            self._in_ld = True
            self._buf = []
        if tag not in SKIP_TAGS:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag == "script" and self._in_ld:
            self._in_ld = False
            self.ldjson.append("".join(self._buf))
        if tag in SKIP_TAGS:
            return
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        elif tag in self.stack:
            # tutup tag yang lupa ditutup
            while self.stack and self.stack.pop() != tag:
                pass
            self.unbalanced.append(tag)

    def handle_data(self, data):
        if self._in_ld:
            self._buf.append(data)


def check_html(path: pathlib.Path) -> None:
    raw = path.read_text(encoding="utf-8")
    p = Scan()
    p.feed(raw)

    dupes = {i for i in p.ids if p.ids.count(i) > 1}
    if dupes:
        ERRORS.append(f"{path.name}: id ganda -> {sorted(dupes)}")
    if p.unbalanced:
        WARN.append(f"{path.name}: tag tidak seimbang -> {sorted(set(p.unbalanced))[:5]}")

    for ref in sorted(set(p.refs)):
        if not (ROOT / ref).exists():
            ERRORS.append(f"{path.name}: referensi hilang -> {ref}")

    for img in p.imgs:
        src = img.get("src", "?")
        if not img.get("alt"):
            ERRORS.append(f"{path.name}: <img> tanpa alt -> {src}")
        if "loading" not in img and "hero" not in src:
            WARN.append(f"{path.name}: <img> tanpa loading=lazy -> {src}")
        if not (img.get("width") and img.get("height")):
            WARN.append(f"{path.name}: <img> tanpa width/height -> {src}")

    for blob in p.ldjson:
        try:
            json.loads(blob)
        except json.JSONDecodeError as exc:
            ERRORS.append(f"{path.name}: JSON-LD tidak valid -> {exc}")


def check_assets() -> None:
    for f in ("sitemap.xml", "robots.txt", "index.html"):
        if not (ROOT / f).exists():
            ERRORS.append(f"file wajib tidak ada -> {f}")

    for js in (ROOT / "js").glob("*.js"):
        r = subprocess.run(["node", "--check", str(js)], capture_output=True, text=True)
        if r.returncode != 0:
            ERRORS.append(f"{js.name}: syntax error -> {r.stderr.strip().splitlines()[:1]}")

    for css in (ROOT / "css").glob("*.css"):
        text = css.read_text(encoding="utf-8", errors="ignore")
        if text.count("{") != text.count("}"):
            ERRORS.append(f"{css.name}: kurung kurawal tidak seimbang")


def check_content() -> None:
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    for anchor in ("#home-section", "#about-section", "#portfolio-section", "#contact-section"):
        if f'id="{anchor[1:]}"' not in html:
            ERRORS.append(f"section hilang -> {anchor}")
    if html.count("<h1") != 1:
        ERRORS.append(f"index.html harus punya tepat 1 <h1>, ada {html.count('<h1')}")


def main() -> int:
    check_html(ROOT / "index.html")
    if (ROOT / "data" / "cv.html").exists():
        check_html(ROOT / "data" / "cv.html")
    check_assets()
    check_content()

    for w in WARN:
        print(f"warn: {w}")
    for e in ERRORS:
        print(f"ERROR: {e}")
    print(f"\n{len(ERRORS)} error, {len(WARN)} warning")
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
