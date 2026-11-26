# LinkedIn — 14 Post Siap Copas

Tempel apa adanya. Semua angka di bawah ini nyata dan bisa dibuktikan dari demo.
Jangan diganti dengan klaim yang tidak ada di portofolio.

---

# A. Checklist sebelum posting (sekali)

- [ ] Headline + About + judul Experience — pakai `CHECKLIST-LINKEDIN.md`
- [ ] **Featured**: tautkan `https://ulil-abshor.my.id`
- [ ] **Projects**: tambahkan Lapor Barang Hilang + Shopify Catalog Sync
- [ ] Tiga skill teratas: `Python · FastAPI · Web Development`
- [ ] Foto profil: muka terlihat, latar polos (recruiter melihat ini dulu)
- [ ] Banner: screenshot salah satu demo, bukan gambar stok
- [ ] "Open to work" → aktif, isi: Python Developer, Web Developer, Remote

# B. Checklist tiap kali posting

- [ ] Jam posting: **20.00–21.00 WIB** (pagi di US Timur, sore di Eropa)
- [ ] Satu post = satu ide. Jangan gabung dua proyek
- [ ] Baris pertama harus berdiri sendiri — itu satu-satunya yang terlihat sebelum "see more"
- [ ] Tautan di dalam post, satu saja
- [ ] 3 hashtag, tidak lebih: `#python #fastapi #buildinpublic`
- [ ] Balas komentar dalam 60 menit pertama — ini yang menentukan jangkauan
- [ ] Jangan tag orang yang tidak kamu kenal
- [ ] Setelah 14 hari: 3× seminggu, bukan tiap hari

---

# C. 14 post

## Hari 1 — Lapor Barang Hilang

```
A lost-and-found board for my neighbourhood. 56 tests for an app most people
would call "small".

The part that took longest wasn't the feed or the search. It was the upload
path: strip EXIF before saving, reject anything that isn't an image, and
rate-limit by IP so one person can't flood the board.

Honeypot field for bots. Hashed admin login. Secure cookies behind a proxy.

Live: lapor.ulil-abshor.my.id

#python #fastapi #buildinpublic
```

## Hari 2 — Shopify Catalog Sync

```
I built a Shopify store that fills itself from a supplier spreadsheet.

47 products, size and colour variants, per-variant inventory — one command.
Re-running creates nothing new: a product is skipped only when title, vendor,
price and stock are all unchanged.

The part that took longest wasn't the import. It was making sold-out products
leave the storefront on their own, and come back when stock returns.

Live: shopify.ulil-abshor.my.id

#shopify #python #automation
```

## Hari 3 — Manga Scraper + Cloudflare R2

```
Three sources, one GUI, zero external dependencies.

The scraper pulls chapters, converts every page to WebP at quality 65, and
multipart-uploads straight to Cloudflare R2.

Quality 65 was not a guess. It is the point where a manga page drops from
~1.2 MB to ~180 KB and still looks identical at reading size.

Portable .exe. No install, no Python on the target machine.

#python #webscraping #cloudflare
```

## Hari 4 — Edge AI Motion Classifier

```
Pose classification running entirely in the browser. No GPU server, no video
upload.

33 3D landmarks per frame, 12–22 ms each. Only ~120 bytes of state events ever
reach the backend — the video never leaves the client's machine.

Jump, crouch, kick, lying down: decided from joint angles and hip displacement,
stabilised by a FIFO buffer and a 300 ms state lock so one bad frame doesn't
flip the state.

MediaPipe + WebAssembly, CodeIgniter 4 on the other side.

#computervision #webassembly #php
```

## Hari 5 — n8n AI Workflow

```
Lead triage in n8n, with the boring parts done properly.

Webhook in → validate → classify intent with an LLM → route → write to Google
Sheets → notify the owner.

Anything that fails goes to a dead-letter branch instead of disappearing.

The dead-letter branch is the part most workflows skip. It is also the only
reason you can debug one at 2 a.m.

#n8n #automation #ai
```

## Hari 6 — Web3 dApp QA

```
Eight defects from one Web3 dApp, found by actually using it.

Wallet sign-in that silently failed on a second attempt. A DEX swap showing a
stale quote after a network switch. A signature request with no timeout, so the
UI hung forever.

None of them crashed the app. All of them would have lost users.

Playwright for the repeatable parts, hand-testing for the rest.

#qa #playwright #web3
```

## Hari 7 — Python Scraper + Proxy Rotation

```
Proxies fail. The scraper should not.

A pool of rotating proxies, 2-second failover to a direct connection, multiple
workers, structured JSON out. When a proxy times out the job keeps going — it
just logs the fallback and moves on.

The lesson: build the fallback before you need it, because you will need it at
the worst possible time.

#python #webscraping #datapipeline
```

## Hari 8 — AI Document Chatbot

```
A chatbot that answers from your own PDFs, and says "I don't know" when the
answer isn't there.

Streamlit + vector search. The hard part is not the retrieval — it is refusing
to answer. A model that invents a clause from a contract is worse than no
chatbot at all.

#rag #python #llm
```

## Hari 9 — Automation Bot

```
112 cycles in 24 hours, 0 failed batches.

Reverse-engineered a private API and wallet-signature login, replaced manual
clicking with a scheduled loop. Every action logged, every failure alerted to
Telegram.

Then the rules that actually matter: never spend below a token floor, never
touch reserved stock, stop immediately on session takeover.

Automation without stop conditions is just a faster way to lose money.

#python #automation #api
```

## Hari 10 — AI Admin for Online Shops

```
A shop admin that answers customer chat from the shop's own catalog — and never
invents a price.

Free-form chat becomes a clean order row: name, variant, qty, total, address,
phone. Replies in ~1.5 seconds. WhatsApp confirmation, then follow-ups at day 1
and day 3.

The customer bot has no access to revenue or order data. Fail-closed allowlist,
rate limit, audit log.

#ai #whatsapp #automation
```

## Hari 11 — Video & Audio Pipeline

```
Captions that land on the right word, and music that gets out of the way.

Whisper for the transcript, FFmpeg for the render, automatic ducking at −10.5 dB
under speech, music trimmed to the length of the voice. One command.

The trick isn't the model. It's measuring where speech actually starts and ends
before you cut.

#ffmpeg #whisper #python
```

## Hari 12 — Auto-Apply Bot

```
An auto-apply bot that sends 12 applications from 33 listings — on purpose.

The interesting part isn't the sending. It's the rate limit and the filtering:
the bot refuses to spray, because a hundred generic applications are worse than
twelve that fit.

Most automation projects fail because nobody defines what not to do.

#python #automation #careertools
```

## Hari 13 — Portfolio Website

```
14 projects. One page that has to make sense in 30 seconds.

What I learned building it: nobody reads a project list. They look at the first
two cards, click one live link, and decide.

So the two live apps with real numbers went to the top, and everything else
became supporting evidence.

ulil-abshor.my.id

#webdevelopment #portfolio #frontend
```

## Hari 14 — Shopify, angka terbaru

```
Two weeks ago I posted about a Shopify store that fills itself from a
spreadsheet. Here is what changed since.

47 products imported, 46 published, 1 automatically hidden at zero stock.
47 tests. Re-runs skip every unchanged row instead of rewriting it.

The update: supplier prices now flow through a 20% markup, and every change is
logged old → new — so the margin is auditable instead of implied.

#shopify #python #buildinpublic
```

---

# D. Setelah 14 hari

- Ganti ke 3× seminggu: Senin, Rabu, Jumat
- Sisipkan satu post "what I learned" setiap dua minggu — itu yang paling banyak dibagikan
- Kalau satu post dapat komentar dari orang luar, balas dan lanjutkan percakapan; jangan hanya like
- Simpan angka yang berubah (jumlah produk, jumlah test) dan pakai di post ulang
