Free Guide · Riset Kompetitor × Claude

# Riset 3 kompetitor dan iklan Meta mereka dalam 45 menit, pakai Claude gratis

Harga, klaim, dan iklan yang sedang mereka jalankan, dirangkum jadi satu Google Sheet plus 3 ide yang bisa langsung kamu tes. 100% tool gratis, tanpa extension berbayar.

30–45 menit · Pemula · Biaya tool: Rp0

<!-- wg:box -->
**Hasil akhirnya:**

- Competitor Snapshot di Google Sheets untuk 3 kompetitor
- Iklan aktif mereka di Meta: angle, tanggal mulai tayang, dan ke mana iklannya mengarah
- 3 celah dan 3 ide tes untuk brand kamu

**Tandanya berhasil:** setiap baris punya link sumber dan tanggal cek, dan setiap ide tes menyebut iklan kompetitor yang jadi dasarnya.

Pakai Claude Pro? Claude in Chrome bisa membaca tab langsung dan mempercepat langkah 2 dan 4. Guide ini tidak membutuhkannya, karena extension itu hanya untuk plan berbayar.
<!-- /wg:box -->

## Riset dalam 5 langkah

Label menu di bawah ditulis sesuai tampilan Claude dan Meta berbahasa Inggris.

### Langkah 1 — Pilih 3 kompetitor

Pilih brand yang jualannya paling mirip dengan kamu: kategori, harga, dan target pembelinya. Brand paling besar di kategorimu belum tentu kompetitor paling relevan.

1. Tulis nama 3 kompetitor, website mereka, dan nama akun Instagram atau Facebook-nya.
2. Buka Google Sheets dan buat sheet kosong bernama **Competitor Snapshot**.

**Hasil yang benar:** daftar 3 kompetitor dan satu sheet kosong yang siap diisi.

### Langkah 2 — Tarik data website kompetitor

1. Di Claude, buka chat baru, klik **+** di kiri bawah, lalu pastikan **Web search** tercentang.
2. Copy **Prompt A** di bawah, isi nama dan website kompetitor pertama, lalu kirim.
3. Ulangi untuk kompetitor kedua dan ketiga, satu pesan per kompetitor.

**Hasil yang benar:** tabel produk dengan harga, klaim utama, dan link sumber untuk setiap baris.

> **Hati-hati:** Cek mata uangnya. Waktu kami tes, Claude mengambil harga dalam dolar dari versi internasional sebuah situs. Kalau kompetitor hanya jualan di Shopee atau Tokopedia, Claude tidak bisa membaca halamannya. Buka tokonya, select all (Ctrl+A), copy, lalu paste teksnya ke Claude.

[SCREENSHOT: screenshots/langkah-2-web-search.png]

### Langkah 3 — Cari kompetitor di Meta Ad Library

Ad Library menampilkan semua iklan yang sedang tayang di Facebook dan Instagram. Siapa pun bisa membukanya, tanpa login.

1. Buka `facebook.com/ads/library`, lalu pilih **Indonesia**.
2. Klik **Ad category**, pilih **All ads**, lalu **APPLY**. Kolom pencarian baru aktif setelah ini.
3. Ketik nama kompetitor, lalu pilih brand-nya di bagian **Advertisers**, bukan baris "Search this exact phrase".

**Hasil yang benar:** halaman brand itu dengan jumlah iklan aktif di atas daftar, misalnya "~670 results".

> **Hati-hati:** Satu brand bisa punya beberapa Page, dan banyak reseller memakai nama brand. Pilih yang followers-nya paling banyak dan handle Instagram-nya resmi. Halaman kosong atau error? Matikan ad blocker untuk facebook.com.

[SCREENSHOT: screenshots/langkah-3-ad-library-advertiser.png]

### Langkah 4 — Copy teks iklannya dan minta Claude menganalisis

Claude tidak bisa membuka link Ad Library, karena Meta memblokir akses otomatis. Teksnya tetap bisa kamu copy.

1. Scroll pelan sampai sekitar 20 sampai 30 iklan tampil.
2. Tekan Ctrl+A lalu Ctrl+C untuk copy semua teks di halaman.
3. Di Claude, matikan **Web search**, copy **Prompt B**, paste teks Ad Library di bagian bawahnya, lalu kirim.

**Hasil yang benar:** jumlah iklan aktif, 3 angle yang paling sering dipakai, iklan yang paling lama jalan, dan ke mana iklannya mengarah.

> **Hati-hati:** Ad Library tidak menunjukkan budget atau hasil iklan. Iklan yang sudah lama jalan hanya petunjuk bahwa iklan itu mungkin berhasil, bukan bukti.

### Langkah 5 — Susun Competitor Snapshot dan 3 ide tes

1. Setelah ketiga kompetitor selesai, kirim **Prompt C** di chat yang sama.
2. Blok tabelnya saja, copy, lalu paste ke sel A1 di sheet kamu.
3. Copy bagian celah dan ide tes ke bawah tabel.

**Hasil yang benar:** satu baris per kompetitor, kolomnya terisi di sel masing-masing, lengkap dengan link sumber dan tanggal cek.

> **Hati-hati:** Kalau kalimat pembuka Claude ikut ter-copy, isinya akan masuk ke baris pertama. Blok mulai dari judul kolom tabel.

[SCREENSHOT: screenshots/langkah-5-paste-sheets.png]

**Checkpoint**

- [ ] 3 kompetitor punya data website dengan link sumber
- [ ] Iklan aktif ketiganya sudah dianalisis
- [ ] Competitor Snapshot ada di Google Sheets, lengkap dengan tanggal cek
- [ ] 3 ide tes yang masing-masing menyebut iklan dasarnya

> Sekarang kamu tahu apa yang dijalankan kompetitor. Ide tes itu baru ada hasilnya kalau benar-benar dibuat jadi iklan dan dites tiap minggu. [Email tim Gwenchana](CTA_URL)

## Prompt kamu

**Prompt A: Data website** (Langkah 2, satu kompetitor per pesan)

```text
Cari di web dan baca halaman produk [NAMA KOMPETITOR] di [WEBSITE KOMPETITOR]. Ambil maksimal 5 produk utama.
Untuk setiap produk tulis: nama produk, harga dalam Rupiah, klaim utama, dan URL halaman sumbernya.
Aturan:
- Pakai versi Indonesia dari situsnya. Kalau harganya dalam mata uang lain, tulis mata uangnya dan jangan dikonversi.
- Jangan menebak. Kalau harga atau klaim tidak ada di halaman, tulis "tidak ditemukan".
Tampilkan sebagai tabel.
```

**Prompt B: Analisis iklan** (Langkah 4, satu kompetitor per pesan)

```text
Di bawah ini teks dari Meta Ad Library untuk advertiser [NAMA KOMPETITOR], negara Indonesia, iklan aktif. Analisis hanya dari teks ini. Jangan menebak.
1. Jumlah iklan aktif (angka "results" di atas daftar).
2. 3 angle atau pesan yang paling sering muncul. Untuk masing-masing, beri satu contoh kalimat iklan dan Library ID-nya.
3. Iklan yang paling lama jalan: Library ID dan tanggal "Started running on".
4. Ke mana iklannya mengarah (website, Shopee, WhatsApp, dan lainnya) dan CTA yang paling sering dipakai.
Ingat: Ad Library tidak menunjukkan budget atau hasil. Sebut iklan yang lama jalan sebagai petunjuk, bukan bukti.

[PASTE TEKS AD LIBRARY DI SINI]
```

**Prompt C: Competitor Snapshot dan ide tes** (Langkah 5)

```text
Gabungkan semua hasil di chat ini jadi satu tabel Competitor Snapshot, satu baris per kompetitor, dengan kolom:
Kompetitor | Produk utama dan harga | Klaim utama | Iklan aktif | Angle iklan teratas | Iklan terlama (tanggal) | Arah iklan | Link sumber | Tanggal cek
Tanggal cek: [TANGGAL HARI INI].
Setelah tabel, tulis 3 celah yang belum diisi kompetitor dan 3 ide tes iklan untuk brand aku, [NAMA BRAND KAMU] yang menjual [PRODUK KAMU]. Setiap ide harus menyebut kompetitor dan Library ID iklan yang jadi dasarnya.
Mulai jawabanmu langsung dari tabel, tanpa kalimat pembuka.
```

## Solusi cepat

<!-- wg:details -->

**1. Claude bilang tidak bisa membaca halamannya**
Toko Shopee, Ad Library, dan situs yang dibangun dengan JavaScript sering tidak terbaca oleh Claude. Buka halamannya sendiri, select all, copy, lalu paste teksnya ke Claude. Kalau teksnya berantakan, upload screenshot lewat **+** > **Add files or photos**.

**2. Hasil Ad Library campur dengan brand lain atau reseller**
Kamu mencari dengan kata kunci, bukan memilih advertiser. Ketik nama brand lagi dan pilih di bagian **Advertisers**. Cek jumlah followers dan handle resminya.

**3. Kena batas pemakaian plan Free**
Halaman panjang dan banyak kompetitor dalam satu chat cepat menghabiskan kuota. Kirim satu kompetitor per pesan, matikan **Web search** saat kamu paste teks, dan tunggu kuotanya reset. Di plan Free, kuota reset setiap lima jam.

<!-- wg:cta -->
## Selanjutnya: dari riset jadi iklan yang dites

Snapshot kamu menunjukkan angle yang dipakai kompetitor dan celah yang bisa kamu isi. Yang tidak bisa dikerjakan sebuah sheet: membuat creative dari ide itu, mengetesnya tiap minggu dengan budget yang terkendali, dan membaca hasilnya dengan tracking yang benar.

Gwenchana mengubah hasil riset seperti ini jadi campaign Meta Ads yang dites rutin, mulai dari paket Starter.

Belum beriklan di Meta, atau masih memvalidasi produk? Jalankan riset ini dulu dan ulangi tiap bulan. Seminggu ke depan kami kirim lewat email: prompt untuk membaca harga dan promo kompetitor, 7 prompt riset lanjutan, dan template brief creative dari iklan kompetitor.

Mau ngobrol dulu? Kirim email ke info@gwenchana.digital, ceritakan brand dan iklan yang sedang kamu jalankan.

[Email Gwenchana soal Meta Ads](CTA_URL)

---

Dicek pada 28 September 2026. Meta dan Claude sering mengubah tampilannya. Kalau ada yang terlihat berbeda, mulai dari bagian solusi cepat.
