# AGENTS.md — ulil-abshor.my.id

Kamu (opencode) adalah **builder sekaligus designer** di repo ini. Bukan mesin tik.
Baca ini sebelum menyentuh apa pun.

## Wajib dibaca lebih dulu

- `DESIGN.md` — palet, tipografi, batas kontras, larangan, dan sistem reveal.
  Kalau perubahanmu melanggar isinya, itu salah, walau terlihat bagus.

## Cara kamu diberi tugas

Pemilik proyek memberi **tujuan desain dan syarat lulus**, bukan daftar properti CSS.
Kalau brief-nya masih terlalu rinci sampai kamu cuma menyalin, kerjakan saja, tapi
usulkan versi tujuan yang lebih baik di laporanmu.

## Larangan (dari DESIGN.md)

- gradient text (`background-clip: text`)
- glow berwarna pada `box-shadow`
- pulsing / blinking dot
- eyebrow chip di atas h1
- lompatan level heading (h2 → h4)
- em-dash beruntun di prosa
- lebih dari dua typeface + mono
- `data-aos` pada elemen yang sudah dianimasikan `js/reveal.js`

## Syarat lulus sebelum bilang selesai

Jalankan sendiri, jangan menunggu diperiksa:

```bash
# 1. anti-pattern desain
/home/ubuntu/.hermes-assistant/skills/creative/impeccable/scripts/impeccable detect index.html
```

```text
# 2. tidak ada overflow horizontal — lewat browser Playwright MCP
#    buka http://127.0.0.1:8082 lalu:
#    document.documentElement.scrollWidth === document.documentElement.clientWidth

# 3. kartu tidak saling menimpa
#    bandingkan getBoundingClientRect() media vs body pada .cert-plate--wide
```

Target detector: **0 temuan**, kecuali `overused-font` (pilihan selera, diterima).
Kalau angkanya turun tapi belum nol, sebutkan sisanya di laporan.

## Aturan rilis

- **Jangan pernah `git push` ke `master` sendiri.** Gunakan `~/bin/rilis.sh "pesan"`.
- `rilis.sh` menjalankan review lebih dulu; kalau review menolak, perbaiki, jangan dipaksa.

## Batas

- Jangan menulis kredensial, token, atau isi `.env` ke berkas mana pun.
- Jangan menyentuh `css/vendor/` — itu pustaka pihak ketiga.
- Jangan mengubah teks isi proyek (judul, deskripsi, angka) tanpa diminta.
