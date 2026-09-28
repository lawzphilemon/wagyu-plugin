# Nurture emails: Meta Ads × Claude (lite)

```
Sequence: Meta Ads × Claude free guide
Trigger: signup on the opt-in page (separate lists or a language field for EN and ID)
Goal: a conversation with Gwenchana about Meta Ads (Starter tier)
Length: 5 emails over 8 days
Timing: day 0, 2, 4, 6, 8 (weekdays; shift weekend sends to Monday)
Exit: the subscriber clicks the premium CTA or replies. Move them to sales follow-up and stop the sequence.
```

Placeholders to swap in your email tool:
- `[FIRST_NAME]`: your tool's merge tag (Mailchimp `*|FNAME|*`, Kit `{{ subscriber.first_name }}`). Use a fallback such as "there" / "kamu".
- `[GUIDE_URL]`: the lite guide page. `[FULL_GUIDE_URL]`: the full guide page (bonus, noindex). `[CTA_URL]`: the premium CTA.
- `[SENDER]`: the person signing the emails.

Rules kept: no invented results, prices, or case studies. Premium details stay at the level of the guide until you add real ones.

---

## English

### E1: Delivery
**Send:** immediately
**Subject:** Your Meta Ads × Claude guide is here
**Preview:** 15 minutes, 5 steps, and a read-only setup so Claude can't touch your budget.

Hi [FIRST_NAME],

Here's the guide you asked for:

**[Open the guide →]([GUIDE_URL])**

In 15 minutes you'll have Claude connected to your Meta ad account and your first performance report from live data.

One tip before you start: do Step 3 first if you're short on time. It takes ten seconds and tells you whether Meta has switched your account on yet. Meta is rolling this out account by account, so it's the most common reason a setup "doesn't work".

Over the next week I'll send you three more pieces: the second safety lock, a weekly audit prompt pack, and how to make Claude's numbers match Ads Manager.

[SENDER]
Gwenchana

**CTA:** Open the guide → [GUIDE_URL]

### E2: The second lock
**Send:** day 2
**Subject:** The second lock most Claude setups skip
**Preview:** Meta's rules block edits on Meta's side. This one blocks them inside Claude too.

Hi [FIRST_NAME],

In Step 4 you blocked agent actions in Meta Business Suite. That's lock one.

Lock two lives in Claude, and it matters for one reason: Claude's Research mode can call connector tools without asking you first.

1. In Claude, go to **Customize** > **Connectors** and click **Meta Ads**.
2. Look for **Tool permissions**. Tools are grouped into read-only and write/delete.
3. Set the write/delete group to **Blocked**. Leave read-only on **Always allow**.

Honest note: Claude documents Tool permissions for Team and Enterprise plans, and we haven't confirmed it on every individual plan yet. If you don't see it, Meta's lock from Step 4 is still doing the job.

Then test both locks. Open a new chat, turn Meta Ads on, and paste:

```
Create a new campaign in ad account act_[AD_ACCOUNT_ID] named WAGYU-TEST with the Traffic objective and leave it paused.
```

Claude should tell you it can't. If a campaign appears anyway, it's paused and hasn't spent anything. Delete it in Ads Manager and recheck the settings.

Why bother? AI with write access and no guardrails is how budgets get burned.

[SENDER]
Gwenchana

**CTA:** Back to the guide → [GUIDE_URL]

### E3: Weekly audit prompts
**Send:** day 4
**Subject:** 12 prompts for your weekly Meta Ads audit
**Preview:** Start every Monday with the same four prompts. The full pack is one click away.

Hi [FIRST_NAME],

The report prompt from the guide tells you where you stand. These tell you what changed.

Paste this once at the top of every audit chat:

```
For this whole chat, act as a read-only Meta Ads analyst. Use only tools that read data and never change anything, even if I ask later. Work on ad account act_[AD_ACCOUNT_ID]. With every number, state the date range, time zone, and attribution setting you used. If data is missing, say so. Don't estimate.
```

Then run these four every week, in this order:

1. **Delivery errors:** anything blocking campaigns, ad sets, or ads.
2. **Weekly snapshot:** last 7 days vs the 7 before, per campaign.
3. **Anomalies:** spikes or drops in CPM, CTR, cost per result, or frequency.
4. **Creative fatigue:** ads with rising frequency and falling CTR over 14 days.

The full pack has all 12 prompts written out, including budget pacing, the change log, benchmarks, tracking health, and a read-only lock checklist for every new ad account:

**[Get the full prompt pack →]([FULL_GUIDE_URL]#your-prompt-pack-a1)**

The prompts show you the problems. Fixing them every week is the actual job.

[SENDER]
Gwenchana

**CTA:** Get the full prompt pack → [FULL_GUIDE_URL]#your-prompt-pack-a1

### E4: Trust the numbers
**Send:** day 6
**Subject:** Why Claude's numbers don't match Ads Manager
**Preview:** It's almost always one of five settings. Here's how to line them up in two minutes.

Hi [FIRST_NAME],

If Claude says 42 purchases and Ads Manager says 38, don't pick a side yet. It's usually one of these:

- Date range (complete days vs including today)
- Time zone (the ad account's, not yours)
- Attribution setting (for example 7-day click vs 1-day click)
- Conversion count (all conversions vs first conversion)
- Currency

The fix:

1. Ask Claude to state all five for its answer.
2. Open **Meta Ads Reporting**, set the same dates, then **Customize** > **Options** > **Select attribution settings**.
3. Pick the setting Claude named, choose **All conversions**, and click **Apply**.

Now compare. If they still don't match after that, the problem usually isn't Claude. It's tracking: a pixel that misses events, or Conversions API not set up. The full guide covers that and nine other fixes:

**[See all troubleshooting →]([FULL_GUIDE_URL]#troubleshooting)**

Data you can't trust makes every AI answer worse. Tracking is a setup job, and it's one of the first things we check.

[SENDER]
Gwenchana

**CTA:** See all troubleshooting → [FULL_GUIDE_URL]#troubleshooting

### E5: The part AI can't do
**Send:** day 8
**Subject:** What Claude can't do for your Meta Ads
**Preview:** It can read the account and spot what's off. Moving the numbers is a different job.

Hi [FIRST_NAME],

By now Claude can read your ad account, spot anomalies, and tell you which campaigns drain budget. That's real progress.

What it can't do is the weekly work that moves the numbers:

- producing fresh creative to test, week after week
- making budget calls that scale without your CPA blowing up
- setting up tracking (Conversions API, attribution) so the data is worth reading

That's what Gwenchana does. We run Meta Ads end to end, starting from the Starter tier, and you keep watching every number with the Claude setup you built.

If you're still testing with a small budget and enjoy running it yourself, keep going on your own for now. The guide and prompts are yours either way.

If you'd rather hand the execution to a team:

**[Talk to Gwenchana about Meta Ads →]([CTA_URL])**

[SENDER]
Gwenchana

**CTA:** Talk to Gwenchana about Meta Ads → [CTA_URL]

---

## Bahasa Indonesia

### E1: Pengiriman guide
**Kirim:** langsung setelah daftar
**Subject:** Guide Meta Ads × Claude kamu sudah siap
**Preview:** 15 menit, 5 langkah, dan setup read-only supaya Claude tidak bisa menyentuh budget kamu.

Hai [FIRST_NAME],

Ini guide yang kamu minta:

**[Buka guide-nya →]([GUIDE_URL])**

Dalam 15 menit, Claude sudah terhubung ke ad account Meta kamu dan kamu pegang laporan performa pertama dari data live.

Satu tips sebelum mulai: kalau waktumu mepet, kerjakan Langkah 3 duluan. Cuma sepuluh detik, dan langsung ketahuan apakah Meta sudah mengaktifkan akunmu. Meta mengaktifkan fitur ini satu per satu per akun, jadi inilah penyebab paling umum setup terlihat "tidak jalan".

Seminggu ke depan aku kirim tiga hal lagi: kunci pengaman kedua, prompt untuk audit mingguan, dan cara menyamakan angka Claude dengan Ads Manager.

[SENDER]
Gwenchana

**CTA:** Buka guide-nya → [GUIDE_URL]

### E2: Kunci kedua
**Kirim:** hari ke-2
**Subject:** Kunci kedua yang sering dilewatkan
**Preview:** Aturan Meta memblokir perubahan di sisi Meta. Yang ini memblokirnya di dalam Claude juga.

Hai [FIRST_NAME],

Di Langkah 4 kamu sudah memblokir aksi agent di Meta Business Suite. Itu kunci pertama.

Kunci kedua ada di Claude, dan alasannya satu: mode Research di Claude bisa memanggil tool connector tanpa minta izin dulu.

1. Di Claude, buka **Customize** > **Connectors**, lalu klik **Meta Ads**.
2. Cari **Tool permissions**. Tool-nya dikelompokkan jadi read-only dan write/delete.
3. Ubah grup write/delete jadi **Blocked**. Biarkan read-only di **Always allow**.

Catatan jujur: Claude mendokumentasikan Tool permissions untuk plan Team dan Enterprise, dan kami belum memastikannya di semua plan individu. Kalau menunya tidak ada, kunci Meta dari Langkah 4 tetap bekerja.

Setelah itu tes kedua kuncinya. Buka chat baru, nyalakan Meta Ads, lalu paste:

```
Buat campaign baru di ad account act_[AD_ACCOUNT_ID] bernama WAGYU-TEST dengan objective Traffic, biarkan statusnya paused.
```

Claude seharusnya bilang tidak bisa. Kalau campaign-nya ternyata terbuat, statusnya paused dan belum memakan biaya. Hapus di Ads Manager, lalu cek ulang pengaturannya.

Kenapa repot-repot? AI yang punya akses mengubah tanpa pengaman adalah cara tercepat budget terbakar.

[SENDER]
Gwenchana

**CTA:** Kembali ke guide → [GUIDE_URL]

### E3: Prompt audit mingguan
**Kirim:** hari ke-4
**Subject:** 12 prompt untuk audit Meta Ads mingguan
**Preview:** Mulai setiap Senin dengan empat prompt yang sama. Paket lengkapnya tinggal satu klik.

Hai [FIRST_NAME],

Prompt laporan dari guide memberi tahu posisi kamu sekarang. Prompt-prompt ini memberi tahu apa yang berubah.

Paste ini sekali di awal setiap chat audit:

```
Sepanjang chat ini, bertindaklah sebagai analis Meta Ads yang hanya membaca data. Pakai tool yang membaca data saja dan jangan pernah mengubah apa pun, walaupun nanti aku minta. Kerjakan di ad account act_[AD_ACCOUNT_ID]. Setiap menyebut angka, sebutkan rentang tanggal, zona waktu, dan setting atribusi yang dipakai. Kalau datanya tidak ada, bilang saja. Jangan menebak.
```

Lalu jalankan empat ini tiap minggu, dengan urutan ini:

1. **Error delivery:** apa pun yang memblokir campaign, ad set, atau iklan.
2. **Snapshot mingguan:** 7 hari terakhir dibanding 7 hari sebelumnya, per campaign.
3. **Anomali:** lonjakan atau penurunan CPM, CTR, cost per result, atau frequency.
4. **Creative fatigue:** iklan dengan frequency naik dan CTR turun dalam 14 hari.

Paket lengkapnya berisi 12 prompt yang sudah ditulis utuh, termasuk pacing budget, riwayat perubahan, benchmark, kesehatan tracking, dan checklist kunci read-only untuk setiap ad account baru:

**[Ambil paket prompt lengkapnya →]([FULL_GUIDE_URL]#your-prompt-pack-a1)**

Prompt-prompt ini menunjukkan masalahnya. Membereskannya tiap minggu, itu pekerjaan yang sebenarnya.

[SENDER]
Gwenchana

**CTA:** Ambil paket prompt lengkapnya → [FULL_GUIDE_URL]#your-prompt-pack-a1

### E4: Angka yang bisa dipercaya
**Kirim:** hari ke-6
**Subject:** Kenapa angka Claude beda dengan Ads Manager
**Preview:** Hampir selalu karena satu dari lima setting. Begini cara menyamakannya dalam dua menit.

Hai [FIRST_NAME],

Kalau Claude bilang 42 pembelian dan Ads Manager bilang 38, jangan buru-buru memilih salah satu. Biasanya penyebabnya salah satu dari ini:

- Rentang tanggal (hari yang sudah lengkap vs termasuk hari ini)
- Zona waktu (milik ad account, bukan milikmu)
- Setting atribusi (misalnya 7-day click vs 1-day click)
- Conversion count (all conversions vs first conversion)
- Mata uang

Cara membereskannya:

1. Minta Claude menyebutkan kelima setting itu untuk jawabannya.
2. Buka **Meta Ads Reporting**, samakan tanggalnya, lalu **Customize** > **Options** > **Select attribution settings**.
3. Pilih setting yang disebut Claude, pilih **All conversions**, lalu klik **Apply**.

Sekarang bandingkan. Kalau masih beda juga, biasanya masalahnya bukan di Claude, tapi di tracking: pixel yang melewatkan event, atau Conversions API yang belum dipasang. Guide lengkapnya membahas ini dan sembilan solusi lain:

**[Lihat semua troubleshooting →]([FULL_GUIDE_URL]#troubleshooting)**

Data yang tidak bisa dipercaya membuat setiap jawaban AI ikut meleset. Tracking itu pekerjaan setup, dan termasuk hal pertama yang kami cek.

[SENDER]
Gwenchana

**CTA:** Lihat semua troubleshooting → [FULL_GUIDE_URL]#troubleshooting

### E5: Bagian yang tidak bisa dikerjakan AI
**Kirim:** hari ke-8
**Subject:** Yang tidak bisa dikerjakan Claude untuk Meta Ads kamu
**Preview:** Claude bisa membaca akun dan menemukan yang tidak beres. Menggerakkan angkanya, itu pekerjaan lain.

Hai [FIRST_NAME],

Sekarang Claude sudah bisa membaca ad account kamu, menemukan anomali, dan menunjukkan campaign mana yang menghabiskan budget. Itu kemajuan nyata.

Yang tidak bisa dilakukannya adalah pekerjaan mingguan yang menggerakkan angka:

- membuat creative baru untuk dites, minggu demi minggu
- mengambil keputusan budget supaya bisa scale tanpa CPA melonjak
- memasang tracking (Conversions API, atribusi) supaya datanya layak dibaca

Itu yang dikerjakan Gwenchana. Kami menjalankan Meta Ads dari hulu ke hilir, mulai dari paket Starter, dan kamu tetap memantau setiap angka lewat setup Claude yang sudah kamu buat.

Kalau kamu masih testing dengan budget kecil dan senang mengerjakannya sendiri, lanjutkan dulu sendiri. Guide dan prompt-nya tetap milikmu.

Kalau kamu lebih suka eksekusinya dipegang tim:

**[Ngobrol dengan Gwenchana soal Meta Ads →]([CTA_URL])**

[SENDER]
Gwenchana

**CTA:** Ngobrol dengan Gwenchana soal Meta Ads → [CTA_URL]

---

## What to measure

| Metric | Watch for |
|---|---|
| E1 open and guide click rate | Low clicks = the opt-in promise and E1 don't match |
| E3 and E4 clicks to the full guide | Tells you which deeper topic readers care about (future guides) |
| E5 CTA clicks and replies | The conversion goal |
| Unsubscribes per email | A spike after one email means that email felt too salesy or too long |
