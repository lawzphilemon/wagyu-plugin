Status: confirmed

# WGY-O — Outline (full): Tracking klik WhatsApp ke GA4 + ChatGPT Ads

Format: full (primary: id, second: en). The page has a public preview, then an email form, then the full guide.
Distribution: promoted with Meta Ads → landing page (public preview) → email form → full guide.

Source keys (full URLs in 02-research.md):
- [OAI-CM] Help: Conversion Measurement · [OAI-MR] Help: Measure Results · [OAI-SETUP] Help: Ads Manager Account Setup
- [OAI-CT] Dev: Conversion Tracking · [OAI-PX] Dev: Measurement Pixel · [OAI-EV] Dev: Supported Events
- [OAI-GTM] github.com/openai/ads-measurement-pixel-gtm-template + GTM gallery listing
- [GTM-CLICK] GTM Help: Click trigger · [GTM-GA4] GTM Help: GA4 events in Tag Manager · [GTM-VARS] Built-in variables
- [GA4-KEY] GA4 Help: Mark events as key events · [GA4-DBG] GA4 Help: DebugView · [GA4-NAME] Event naming rules
- [WPR] WP Rocket docs · [WA] WhatsApp click to chat (snippet) · [FRICTION] research section 3
- USER = 05-stepcheck.md, Gwenchana account, 2026-10-08

══════════ PUBLIC (above the email form) ══════════

HERO
  Eyebrow: Panduan Gratis · ChatGPT Ads × WhatsApp
  Title: Lacak klik WhatsApp dari iklan ChatGPT di GA4 dan OpenAI Ads dalam 60 menit
  Subtitle: Untuk owner dan marketer yang menerima lead lewat WhatsApp. Satu trigger GTM, dua tujuan, tanpa menulis kode. 100% tool gratis, budget iklan terpisah.
  Chips: 45–60 menit · Level menengah · Biaya tool: Rp0

RESULT PREVIEW
  At the end you have:
  - Trigger GTM yang menangkap semua format link WhatsApp
  - Event `whatsapp_click` di GA4, sudah jadi key event
  - Pixel OpenAI lewat template resmi OpenAI, mengirim `page_viewed` dan `lead_created`, dan Lead Created terpasang di campaign
  - Pola UTM untuk campaign ChatGPT Ads
  Success check: satu klik tes di tombol WhatsApp → (1) `whatsapp_click` muncul di GA4 DebugView, (2) `lead_created` muncul di Ads Manager → Conversions → Event Stream dalam beberapa menit.
  Honest line: yang dilacak adalah klik tombol (niat menghubungi), bukan chat yang benar-benar terkirim.

FOR / NOT FOR
  For:
  - Bisnis yang lead utamanya masuk lewat tombol WhatsApp di website
  - Sudah atau akan beriklan di ChatGPT Ads dan ingin tahu iklan mana yang menghasilkan chat
  - Sudah pegang akses admin GTM dan GA4
  Not for:
  - Website belum memakai GTM (pasang dulu, link panduan resmi Google)
  - Butuh tracking chat yang benar-benar terkirim atau closing (perlu WhatsApp Business API/CRM, di luar panduan ini)
  - Butuh server-side / Conversions API (panduan terpisah)

TOOLKIT
  | Tool | Dipakai untuk | Batas gratis (dicek 8 Okt 2026) | Akun |
  |---|---|---|---|
  | Google Tag Manager | Trigger dan semua tag | Gratis | Akun Google, container terpasang |
  | Google Analytics 4 | `whatsapp_click`, key event, DebugView | Gratis, maks. 30 key event per property | Peran Marketer atau lebih |
  | OpenAI Ads Manager | Pixel, conversion event, Event Stream | Gratis membuat akun dan data source; iklan baru tayang setelah verifikasi dan billing | Akun OpenAI Ads |
  | Template "OpenAI Ads Measurement Pixel" (by openai) | Pixel tanpa kode | Gratis, template resmi OpenAI di GTM Gallery | — |
  | Tag Assistant (GTM Preview) | Tes sebelum publish | Gratis | Akun Google |
  Prerequisites: GTM terpasang dan GA4 jalan lewat GTM; tombol WhatsApp berupa link (`<a href>`); akun OpenAI Ads Manager.
  Note on verification: data source bisa dibuat sebelum NPWP dan billing selesai (dicek Okt 2026). Akun bisnis butuh NPWP, akun personal tidak; dua-duanya verifikasi identitas sebelum iklan tayang. `[VERIFY: identitas sebelum data source]`

PHASE OVERVIEW (3 lines, teaser for the form)
  Fase 1 Ads Manager (~15 menit) · Fase 2 GTM + GA4 (~20 menit) · Fase 3 Pixel OpenAI + tes (~20 menit)

══════════ EMAIL FORM ══════════
  "Masukkan email untuk membuka panduan lengkap" (form is handled on the user's WordPress side; /finaldraft marks the split point)

══════════ GATED (full guide) ══════════

PHASE 1: Siapkan Ads Manager (~15 menit)
  Goal: Pixel ID di tangan, conversion event Lead created ada dan terpasang di campaign, UTM terpasang.

  Step 1.1: Salin Pixel ID
    1. Ads Manager → **Conversions** (menu sendiri di sidebar, bukan di bawah Tools)
    2. Tab **Data Source** → salin kode di bawah nama data source
    3. Belum ada data source → **+ Create → Data Source**, Type Web `[VERIFY: isi dialog]`
    — Source: [OAI-PX] ("Create a new Pixel ID in the conversions tab"), USER (A)
    — Expected result: Pixel ID tersalin (format huruf-angka, contoh di template: px_123)
    — Pitfall: tutorial lain menulis "Tools → Conversions", jalur itu sudah usang (USER)
    — Screenshot: halaman Conversions dengan 4 tab (blur Pixel ID)

  Step 1.2: Buat conversion event Lead created
    1. **+ Create → Conversion Event** → dialog **Create custom conversion**
    2. **Data source** = pixel kamu · **Base event** = **Lead created** · **Conversion name** maks. 30 karakter (Aset B)
    3. **Create**
    — Source: [OAI-CT] (lead_created untuk "requests contact"), [OAI-EV], USER (C)
    — Expected result: Lead Created muncul di tab **Conversion Events**
    — Pitfall: judul dialog tertulis "custom" walaupun event-nya standar, abaikan. Jangan pilih App installed/App opened (tidak didukung pixel website).
    — Screenshot: dialog Create custom conversion

  Step 1.3: Pasang Lead Created ke campaign
    1. **Campaigns** → ⋯ di baris campaign → **Edit Campaign**
    2. **Conversion event** → pilih Lead Created; hapus Page Viewed kalau ikut terpasang (tombol ✕)
    3. **Save**
    — Source: [OAI-MR] FAQ (event harus cocok dengan campaign, tidak dihitung ulang), [OAI-CT], USER (C)
    — Expected result: tab Conversion Events menunjukkan Lead Created "Used by 1 campaign"
    — Pitfall: pasang **sebelum** iklan tayang; klik lama tidak dihitung ulang (USER: Lead Created dibuat setengah hari setelah iklan jalan). Kolom Conversions menjumlahkan semua event yang terpasang, jadi Page Viewed membuat angkanya menggelembung. Belum punya campaign → pilih Lead Created saat membuat campaign.
    — Screenshot: field Conversion event di Edit Campaign

  Step 1.4: Pasang UTM lewat Tracking parameters
    1. Masih di **Edit Campaign** → **Tracking parameters**
    2. Tempel Aset C → **Save**
    — Source: USER (J: label, placeholder yang didukung), [OAI-MR] FAQ (urutan prioritas Ad URL → Ad → Ad Group → Campaign)
    — Expected result: string UTM tersimpan di campaign
    — Pitfall: label di UI adalah "Tracking parameters", bukan "Landing page query parameters" seperti di Help Center. `[VERIFY: UTM sampai ke GA4 setelah klik iklan sungguhan]`
    — Screenshot: field Tracking parameters

  CHECKPOINT 1:
    [ ] Pixel ID tersalin
    [ ] Lead Created ada dan "Used by 1 campaign"
    [ ] Page Viewed tidak terpasang sebagai konversi
    [ ] Tracking parameters terisi
  Ladder point: None

PHASE 2: Kirim klik WhatsApp ke GA4 (~20 menit)
  Goal: satu trigger WhatsApp dan event `whatsapp_click` yang sudah jadi key event.

  Step 2.1: Aktifkan Click URL
    1. GTM → **Variables** → Built-In Variables → **Configure**
    2. Centang **Click URL**
    — Source: [GTM-VARS], USER (F), [FRICTION] #1
    — Expected result: Click URL ada di daftar Built-In Variables
    — Pitfall: tanpa Click URL, trigger tidak pernah cocok dan diam saja
    — Screenshot: panel Configure Built-In Variables

  Step 2.2: Buat trigger klik WhatsApp
    1. **Triggers → New → Trigger Configuration → Just Links** (ID: Hanya Link)
    2. **Some Link Clicks** → `Click URL` · `matches RegEx (ignore case)` · Aset A
    3. Nama: `WA - Klik WhatsApp` → **Save**
    — Source: [GTM-CLICK], [WA], [FRICTION] #3
    — Expected result: trigger tersimpan
    — Pitfall: "Wait for Tags" biarkan mati dulu `[VERIFY: G]`. Tombol dari widget dalam iframe tidak tertangkap → Troubleshooting.
    — Screenshot: konfigurasi trigger dengan regex

  Step 2.3: Buat tag GA4 `whatsapp_click`
    1. **Tags → New → Google Analytics: GA4 Event**
    2. **Measurement ID** · **Event Name** `whatsapp_click`
    3. Triggering → `WA - Klik WhatsApp` → nama `GA4 - whatsapp_click` → **Save**
    — Source: [GTM-GA4], [GA4-NAME]
    — Expected result: tag tersimpan
    — Pitfall: nama event peka huruf besar-kecil, tanpa spasi, maks. 40 karakter
    — Screenshot: konfigurasi tag GA4

  Step 2.4: Tandai `whatsapp_click` sebagai key event
    1. GA4 **Admin → Data display → Events → + Create event**
    2. Nama `whatsapp_click` → toggle **Mark as key event** → **Create**
    3. Event sudah muncul di daftar → cukup klik ikon bintang
    — Source: [GA4-KEY]
    — Expected result: `whatsapp_click` terdaftar sebagai key event
    — Pitfall: GA4 juga mencatat event `click` bawaan untuk klik yang sama (USER); yang ditandai adalah `whatsapp_click`. Laporan standar butuh sampai 24 jam.
    — Label ID: `[VERIFY: H]`
    — Screenshot: create key event

  CHECKPOINT 2:
    [ ] Click URL aktif
    [ ] Trigger `WA - Klik WhatsApp` tersimpan
    [ ] Tag `GA4 - whatsapp_click` tersimpan
    [ ] `whatsapp_click` ditandai key event
  Ladder point: None

PHASE 3: Pasang pixel OpenAI, tes, publish (~20 menit) `[VERIFY: E, D untuk 3.1–3.4, dites setelah 2026-10-13]`
  Goal: dua tag OpenAI dari template resmi, lolos success check, container live.

  Step 3.1: Tambahkan template resmi OpenAI
    1. **Templates → Tag Templates → Search Gallery** → ketik "OpenAI"
    2. Pilih **OpenAI Ads Measurement Pixel** (by openai) → **Add to workspace** → setujui permission
    — Source: [OAI-GTM] (gallery listing dicek 8 Okt 2026)
    — Expected result: template muncul di Tag Templates
    — Pitfall: ada beberapa template OpenAI di gallery (Stape, Webaround); pilih yang by **openai**
    — Screenshot: hasil pencarian gallery

  Step 3.2: Simpan Pixel ID sebagai konstanta
    1. **Variables → User-Defined Variables → New → Constant**
    2. Tempel Pixel ID → nama `Const - OpenAI Pixel ID` → **Save**
    — Source: USER (pola variabel konstanta di container Gwenchana), [OAI-GTM] ("Use the same Pixel ID for every… tag")
    — Expected result: satu variabel Pixel ID untuk semua tag OpenAI
    — Pitfall: None
    — Screenshot: None

  Step 3.3: Buat tag Page viewed
    1. **Tags → New** → template OpenAI Ads Measurement Pixel
    2. **Pixel ID** = `{{Const - OpenAI Pixel ID}}` · **Event name** = Page viewed
    3. Trigger **All Pages** → nama `OpenAI - Page viewed` → **Save**
    — Source: [OAI-GTM] ("Event tags initialize the pixel themselves, so the base tag is not required"), [OAI-EV]
    — Expected result: tag tersimpan
    — Pitfall: tidak perlu tag "base" terpisah `[VERIFY: D]`
    — Screenshot: konfigurasi tag (blur Pixel ID)

  Step 3.4: Buat tag Lead created
    1. Template yang sama, **Event name** = **Lead created**
    2. Trigger `WA - Klik WhatsApp` → nama `OpenAI - Lead created` → **Save**
    — Source: [OAI-GTM], [OAI-PX] (lead_created, data customer_action)
    — Expected result: tag tersimpan
    — Pitfall: kosongkan Amount dan Currency
    — Screenshot: konfigurasi tag Lead created

  Step 3.5: Matikan tag OpenAI lama
    1. Cari tag Custom HTML atau template lain yang memuat pixel OpenAI → **Pause**
    — Source: [OAI-GTM], Stape doc ("only one Pixel ID is supported on the page"), USER (pitfall pixel dobel)
    — Expected result: hanya dua tag OpenAI yang aktif
    — Pitfall: pixel dobel = event terkirim dua kali
    — Screenshot: None

  Step 3.6: Tes di Preview
    1. **Preview** → masukkan URL → **Connect** → klik tombol WhatsApp
    2. Tag Assistant: event **Link Click**, tag GA4 dan OpenAI "Fired 1 time"
    3. GA4 **Admin → DebugView** → `whatsapp_click`
    4. Ads Manager **Conversions → Event Stream** (polling aktif) → `lead_created`, API Channel `pixel_sdk`
    — Source: [GTM-GA4], [GA4-DBG], [OAI-CT] (monitoring ±15 menit terakhir), USER (success check lolos 8 Okt 2026)
    — Expected result: success check terpenuhi
    — Pitfall: Event Stream hanya menampilkan event ±15 menit terakhir `[VERIFY: event Preview sampai ke OpenAI sebelum publish]`
    — Screenshot: Tag Assistant Tags fired, DebugView, Event Stream

  Step 3.7: Publish dan tes ulang di situs live
    1. **Submit → Publish and Create Version** → nama versi → **Publish**
    2. Buka situs biasa (tanpa Preview) → klik WhatsApp → cek Event Stream sekali lagi
    — Source: [GTM-GA4] (publish), USER
    — Expected result: `lead_created` dari situs live muncul di Event Stream
    — Pitfall: kolom Conversions di laporan baru terisi 24–48 jam ([OAI-MR])
    — Screenshot: None

  CHECKPOINT 3 (= success check):
    [ ] `whatsapp_click` muncul di DebugView
    [ ] `lead_created` muncul di Event Stream
    [ ] Hanya dua tag OpenAI yang aktif
    [ ] Container sudah di-publish
  Ladder point: Soft (1–2 kalimat: tracking jalan; membaca dan menindaklanjuti datanya tiap minggu adalah pekerjaan berikutnya)

ASSETS
  A. Regex trigger WhatsApp (copy block):
     `wa\.me|api\.whatsapp\.com|web\.whatsapp\.com|^whatsapp:`
  B. Nama standar (copy block): Trigger `WA - Klik WhatsApp` · Tag `GA4 - whatsapp_click` · Tag `OpenAI - Page viewed` · Tag `OpenAI - Lead created` · Variabel `Const - OpenAI Pixel ID` · Conversion name `Lead WhatsApp`
  C. UTM untuk Tracking parameters (copy block):
     `utm_source=chatgpt_ads&utm_medium=cpc&utm_campaign=<nama-campaign>&utm_content={ad_id}&utm_term={ad_group_id}`
     Placeholder yang didukung (USER): {campaign_id}, {ad_group_id}, {ad_id}, {ad_account_id}, {oppref}. `chatgpt_ads` memisahkan iklan dari traffic organik ChatGPT di GA4.
  D. Checklist tes 2 menit (copy block): Preview → klik WA → Link Click + 2 tag fired → DebugView `whatsapp_click` → Event Stream `lead_created` → Publish → ulang di situs live.

TROUBLESHOOTING
  1. Trigger tidak jalan → Click URL belum aktif (Step 2.1). [FRICTION #1]
  2. Tombol dari widget (Elfsight, Join.chat, dll.) tidak tertangkap → widget di dalam iframe; minta widget push ke dataLayer atau ganti jadi link biasa. Tombol dibuat lewat JavaScript → coba trigger All Elements. [FRICTION #2]
  3. Sebagian klik tidak tercatat → format link di luar regex (api.whatsapp.com, web.whatsapp.com, whatsapp://). [FRICTION #3]
  4. Tag "Fired" di Preview tapi DebugView kosong → Measurement ID salah, consent belum diberikan, debug mode mati. [FRICTION #4, GA4-DBG]
  5. Pixel terpasang tapi Event Stream kosong → tag Lead created tidak terpicu, Content Security Policy memblokir `bzrcdn.openai.com` / `bzr.openai.com`, atau snippet dari blog memakai URL loader yang salah (template resmi menghindari ini). [FRICTION #5, OAI-PX]
  6. Event masuk tapi Conversions 0 → Lead Created belum terpasang di campaign, dipasang setelah klik terjadi, atau masih jeda 24–48 jam. Lihat angka per event: ikon kolom → **Customize columns** → Events → Lead Created → **Save changes** (USER). [OAI-MR]
  7. Event hilang di WordPress dengan WP Rocket → "Delay JavaScript execution" menunda GTM sampai ada interaksi; centang **Google Tag Manager** di One-click exclusions → Analytics & Ads. [WPR]
  8. Event terhitung dua kali → pixel dobel (template + Custom HTML lama). [Step 3.5]
  9. Dua warning di **Conversions → Diagnostics** (USER, teks persis):
     - "No recent server-to-server events": wajar, setup ini hanya memakai pixel (belum ada Conversions API).
     - "Some events are missing user data" (Email/External ID coverage 0%): wajar, klik WhatsApp tidak membawa email atau ID pelanggan.
     Keduanya tidak menghentikan tracking. Memperbaikinya = Conversions API, panduan berikutnya.
  10. Angka GA4 dan Ads Manager beda → beda atribusi, zona waktu, consent, pemblokir iklan; "A difference does not necessarily indicate an error." Bandingkan rentang tanggal dan zona waktu yang sama. [OAI-CM, OAI-MR]

NEXT WALL + PREMIUM (closing)
  Wall: tracking sudah jalan, tapi datanya harus dibaca dan ditindaklanjuti tiap minggu: ad group dan context hints mana yang menghasilkan klik WA, kapan pause iklan, kapan pindah ke bidding konversi (objective tidak bisa diubah setelah campaign dibuat; USER + [OAI-CT]), dan bagaimana menghubungkan klik WA dengan chat yang benar-benar jadi klien.
  Bridge: Layanan Digital Advertising Gwenchana: strategi dan setup campaign, pembuatan iklan, targeting, pemantauan dan optimasi performa, laporan analitik bulanan.
  Not for: baru ingin mencoba ChatGPT Ads sekali dengan budget kecil, atau belum punya budget iklan rutin tiap bulan. Jalankan panduan ini dan baca datanya sendiri dulu.
  CTA → https://gwenchana.digital/id/services/digital-advertising-services/
  Rules: no prices, no campaign results, byline Lawrence.

FOLLOW-UP EMAILS (USER confirmed 2026-10-08: use 3 emails)
  E1 delivery + link; E2 day 3 "sudah jalan?" check + top 3 fixes; E3 day 7 wall → Gwenchana Digital Advertising.

Ladder points: 2 (after Checkpoint 3, the close). Max allowed 3.

Open [VERIFY] items carried to /stepcheck: Create Data Source dialog · identity verification before data source · G Wait for Tags · H Indonesian GTM/GA4 labels · E/D official template steps 3.1–3.4 (after 2026-10-13) · Preview events before publish · UTM via Tracking parameters reaching GA4.
