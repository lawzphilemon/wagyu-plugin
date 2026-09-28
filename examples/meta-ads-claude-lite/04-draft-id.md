Free Guide · Meta Ads × Claude

# Hubungkan Claude ke akun Meta Ads kamu dalam 15 menit

Laporan performa dari data live, dalam mode read-only, jadi Claude tidak bisa menyentuh budget kamu. 100% tool gratis. Budget iklan tetap terpisah.

15 menit · Ramah pemula · Biaya tool: Rp0

<!-- wg:box -->
**Hasil akhirnya:**

- Claude terhubung ke connector Ads resmi dari Meta
- Kunci read-only di sisi Meta, jadi Claude cuma bisa melihat, tidak bisa mengubah
- Laporan performa pertama, dari prompt yang bisa kamu pakai ulang tiap minggu

**Tandanya berhasil:** Claude menjawab prompt laporan dengan angka campaign kamu yang asli.
<!-- /wg:box -->

## Hubungkan dalam 5 langkah

Label menu di bawah ditulis sesuai tampilan Claude dan Meta berbahasa Inggris.

### Langkah 1 — Tambahkan connector Meta di Claude

1. Di Claude, buka **Customize** di menu kiri, lalu **Connectors**.
2. Klik **+** di kanan atas panel Connectors, lalu pilih **Add custom connector**.
3. Ketik `Meta Ads` di kolom pertama, lalu paste alamat ini di kolom kedua:

```text
https://mcp.facebook.com/ads
```

4. Biarkan **Advanced settings** kosong, lalu klik **Add**.

**Hasil yang benar:** Meta Ads muncul di bagian **Not connected**, dengan badge **CUSTOM**.

> **Hati-hati:** Plan Free Claude cuma boleh punya satu custom connector. Kalau sudah ada satu, hapus dulu.

[SCREENSHOT: screenshots/step-1.3-connector-form.png]

### Langkah 2 — Login Facebook dan pilih satu portfolio

1. Klik **Meta Ads**, lalu **Connect**.
2. Login pakai akun Facebook yang mengelola ad account kamu. Tidak muncul apa-apa? Izinkan pop-up untuk claude.ai, lalu klik **Connect** lagi.
3. Saat Meta menanyakan business portfolio mana yang mau dibagikan, centang satu saja yang akan kamu pakai.

**Hasil yang benar:** Meta Ads berstatus terhubung.

> **Hati-hati:** [VERIFY] Claude bisa mengakses semua portfolio yang kamu centang, termasuk akun klien. Untuk agency: centang satu saja.

[SCREENSHOT: layar pemilihan portfolio]

### Langkah 3 — Cek apakah Meta sudah mengaktifkan akunmu

Meta mengaktifkan fitur ini satu per satu per akun. Cek ini cuma butuh sepuluh detik, dan menyelamatkan kamu dari mengutak-atik setup yang sebenarnya sudah benar.

1. Buka chat baru, klik **+** di kiri bawah, buka **Connectors**, lalu nyalakan **Meta Ads**.
2. Paste prompt **cek akun** di bawah, lalu kirim.

**Hasil yang benar:** ad account kamu muncul dengan `is_ads_mcp_enabled: true`.

> **Hati-hati:** [VERIFY] Kalau hasilnya `false`, setup kamu tidak salah. Meta saja yang belum mengaktifkan akun itu. Lihat solusi cepat nomor 1.

[SCREENSHOT: jawaban cek akun]

### Langkah 4 — Kunci jadi read-only

Saat login, Claude juga ikut dapat izin untuk mengedit campaign. Satu pengaturan di sisi Meta mencabut izin itu. Kamu butuh akses full control ke business portfolio.

1. Di Meta Business Suite, buka **Settings**, lalu **Ads MCP server** di bagian **Integrations**.
2. Pilih ad account kamu, lalu ubah semua aksi jadi **Blocked**.
3. Tes kuncinya: di chat baru, minta Claude "buat campaign paused bernama WAGYU-TEST di act_[AD_ACCOUNT_ID]".

**Hasil yang benar:** **Take actions in this ad account** berstatus blocked, dan Claude melaporkan permintaannya ditolak.

> **Hati-hati:** [VERIFY] Tidak ada **Ads MCP server** di pengaturanmu? Meta masih menggulirkannya bertahap. Sampai muncul, jangan minta Claude mengubah apa pun. Kunci kedua, yang ada di dalam Claude, kami kirim lewat email dua hari lagi. Kalau campaign tes ternyata terbuat, statusnya paused dan belum makan biaya. Hapus saja di Ads Manager.

[SCREENSHOT: aturan Ads MCP server, semua blocked]

### Langkah 5 — Jalankan laporan performa pertama

1. Copy prompt **laporan performa pertama** di bawah.
2. Ganti `[AD_ACCOUNT_ID]` dengan nomor dari Langkah 3 (tanpa `act_`), lalu kirim.

**Hasil yang benar:** tabel ringkasan, peringkat campaign, dan tiga opsi untuk kamu putuskan. Di bagian atas, Claude menyebutkan tanggal, zona waktu, dan setting atribusi yang dipakai.

> **Hati-hati:** Angkanya beda dengan Ads Manager? Samakan tanggal dan setting atribusi di Ads Manager dengan yang disebut Claude, lalu bandingkan lagi.

[SCREENSHOT: contoh laporan, diberi label ilustrasi]

**Checkpoint**

- [ ] Meta Ads terhubung di Claude
- [ ] `is_ads_mcp_enabled: true` untuk akunmu
- [ ] Semua aksi sudah blocked di Business Suite
- [ ] Laporan pertama sudah di tangan

> Sekarang kamu bisa melihat apa yang terjadi di akunmu. Hasilnya datang dari eksekusi tiap minggu, dan bagian itu tidak bisa diserahkan ke AI. [Lihat cara Gwenchana menjalankannya](CTA_URL)

## Prompt kamu

**Cek akun** (Langkah 3)

```text
Pakai connector Meta Ads, tampilkan semua ad account yang bisa aku akses, lengkap dengan nama, account ID, mata uang, zona waktu, dan is_ads_mcp_enabled (sertakan alasannya kalau false). Hanya baca data. Jangan ubah apa pun.
```

**Laporan performa pertama** (Langkah 5, pakai ulang tiap minggu)

```text
Analisis read-only. Jangan ubah apa pun di akun.
Ad account: act_[AD_ACCOUNT_ID]. Periode: 30 hari terakhir yang sudah lengkap.
Di bagian atas, sebutkan tanggal persisnya, zona waktu, setting atribusi, dan mata uang yang kamu pakai.

1. Ringkasan: satu tabel berisi spend, impressions, reach, CPM, CTR, CPC, results, cost per result, dan ROAS kalau ada.
2. Campaign: urutkan berdasarkan cost per result, dari terbaik ke terburuk, dengan spend dan results. Tandai yang performanya paling bagus dan yang paling boros budget.
3. Iklan: 3 terbaik dan 3 terburuk berdasarkan cost per result, masing-masing dengan satu kalimat alasan.
4. Masalah: 3 masalah yang paling banyak menghabiskan uang, lengkap dengan angkanya.
5. Untuk aku putuskan: 3 opsi untuk 7 hari ke depan. Jelaskan perubahannya, jangan dijalankan.
Jawab singkat. Utamakan tabel daripada paragraf. Jawab dalam bahasa Indonesia.
```

## Solusi cepat

<!-- wg:details -->

**1. Claude terhubung, tapi panggilan ke Meta gagal atau muncul `is_ads_mcp_enabled: false`**
Meta belum mengaktifkan ad account itu, dan kamu tidak bisa menyalakannya sendiri. Coba ad account lain yang kamu kelola, lalu jalankan cek akun lagi setiap satu atau dua minggu. Abaikan pihak yang menawarkan jasa "aktivasi" berbayar.

**2. Login Facebook tidak pernah muncul**
Browser kamu memblokir pop-up. Izinkan pop-up untuk claude.ai, lalu klik **Connect** lagi.

**3. Tadinya jalan berminggu-minggu, lalu berhenti**
Akses dari Meta kedaluwarsa setelah sekitar 60 hari. Putuskan Meta Ads di **Customize** > **Connectors**, lalu hubungkan lagi.

<!-- wg:cta -->
## Selanjutnya: bagian yang tidak bisa dikerjakan AI

Claude sekarang bisa membaca akunmu dan menunjukkan apa yang tidak beres. Hasilnya tetap datang dari apa yang kamu kerjakan tiap minggu: creative baru untuk dites, keputusan budget yang tidak bikin CPA melonjak, dan tracking yang bisa dipercaya.

Gwenchana menjalankan Meta Ads dari hulu ke hilir, mulai dari paket Starter, sementara kamu tetap memantau setiap angka lewat setup ini.

Masih testing dengan budget kecil dan senang mengerjakannya sendiri? Lanjutkan dulu sendiri. Seminggu ke depan kami kirim lewat email: kunci pengaman kedua, 12 prompt untuk audit mingguan, dan cara menyamakan angka Claude dengan Ads Manager.

[Ngobrol dengan Gwenchana soal Meta Ads](CTA_URL)

---

Dicek pada 28 September 2026. Meta dan Claude sering mengubah tampilan ini. Kalau ada yang terlihat berbeda, mulai dari bagian solusi cepat.
