import discord, random, os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Bot buatan oleh Usaid Muhammad Hail, tentang perubahan iklim dan edukasi lingkungan. Bot ini menyediakan materi, kuis, tips, dan sumber daya terkait perubahan iklim.

Tips1 = [
    "Gunakan lampu LED yang hemat energi di rumah Anda.",  
    "Kurangi penggunaan kendaraan pribadi dan gunakan transportasi umum atau bersepeda.",
    "Daur ulang barang-barang yang bisa didaur ulang untuk mengurangi limbah.",
    "Tanam pohon atau dukung program penanaman pohon untuk menyerap CO2.",
    "Kurangi konsumsi daging dan pilih makanan berbasis tanaman untuk mengurangi jejak karbon."
]

Tips2 = [
    "Matikan lampu dan peralatan elektronik saat tidak digunakan.",
    "Gunakan peralatan listrik yang efisien energi.",
    "Atur suhu AC dan pemanas dengan bijak untuk menghemat energi.",
    "Gunakan timer atau smart plug untuk mengontrol penggunaan listrik.",
    "Perbaiki kebocoran udara di rumah untuk menjaga suhu tetap stabil."
]
Tips3 = [
    "Bawa tas belanja sendiri untuk mengurangi penggunaan kantong plastik sekali pakai.",
    "Gunakan botol air yang dapat digunakan kembali untuk mengurangi limbah plastik.",
    "Hindari produk dengan kemasan plastik berlebihan.",
    "Dukung perusahaan yang menggunakan kemasan ramah lingkungan.",
    "Daur ulang plastik yang bisa didaur ulang untuk mengurangi limbah."
]
Tips4 = [
    "Gunakan transportasi umum atau bersepeda untuk mengurangi emisi gas rumah kaca.",
    "Pilih kendaraan yang efisien bahan bakar atau listrik.",
    "Hindari penerbangan yang tidak perlu dan pilih opsi transportasi yang lebih ramah lingkungan.",
    "Dukung kebijakan pemerintah yang mendorong penggunaan transportasi berkelanjutan.",
    "Cari alternatif transportasi yang lebih hijau saat bepergian."
]
Tips5 = [
    "Dukung kebijakan yang memprioritaskan tindakan terhadap perubahan iklim.",
    "Ikuti gerakan sosial dan kampanye untuk meningkatkan kesadaran tentang perubahan iklim.",
    "Beri dukungan finansial kepada organisasi yang bekerja untuk melindungi lingkungan.",
    "Pilih produk dan layanan dari perusahaan yang memiliki komitmen terhadap keberlanjutan.",
    "Ikut serta dalam proses pengambilan keputusan publik untuk mendukung kebijakan hijau."
]
questions = {
    "Apa itu perubahan iklim?": ["A. Perubahan iklim adalah peningkatan suhu global yang berlangsung selama puluhan hingga ratusan tahun","B. Perubahan iklim adalah perubahan jangka panjang pada pola cuaca dan suhu rata-rata bumi yang berlangsung selama puluhan hingga ratusan tahun", "C. Perubahan iklim adalah penurunan suhu global yang berlangsung selama puluhan hingga ratusan tahun", "D. Perubahan iklim adalah perubahan jangka pendek pada pola cuaca dan suhu rata-rata bumi yang berlangsung selama beberapa bulan"],
    "Apa penyebab utama perubahan iklim?": ["A. Pembakaran bahan bakar fosil","B. Deforestasi","C. Aktivitas industri","D. Semua di atas"],
    "Apa dampak perubahan iklim?": ["A. Mencairnya es di kutub","B.Terjadinya gempa bumi di dasar laut", "C. Meningkatnya populasi hewan laut", "D. Berkurangnya curah hujan di daerah tropis"],
    "Bagaimana deforestasi mempengaruhi perubahan iklim?": ["A. Mengurangi penyerapan CO2","B. Meningkatkan produksi oksigen","C. Menurunkan suhu global","D. Mengurangi kadar gas rumah kaca"],
    "Manakah sumber energi terbarukan berikut?": ["A. Batu bara","B. Minyak bumi","C. Tenaga surya","D. Gas alam"],
    "Apa yang bisa dilakukan individu untuk menghemat air?": ["A. Mencuci mobil setiap hari","B. Memperbaiki kebocoran keran","C. Menyiram tanaman dengan selang saat panas","D. Membuang sampah ke sungai"],
    "Apa dampak kenaikan permukaan laut?": ["A. Banjir di pesisir","B. Peningkatan jumlah salju","C. Penurunan kadar CO2","D. Pembentukan gunung berapi"],
    "Mengapa penggunaan kendaraan listrik ramah lingkungan?": ["A. Karena tidak memerlukan listrik","B. Karena tidak menghasilkan emisi knalpot","C. Karena lebih mahal","D. Karena lebih cepat"],
    "Apa fungsi panel surya?": ["A. Mengubah panas menjadi bahan bakar","B. Menyimpan air hujan","C. Menghasilkan listrik dari cahaya matahari","D. Menangkap angin"],
    "Manakah dari berikut ini yang merupakan gas rumah kaca?": ["A. Nitrogen","B. Oksigen","C. Karbon dioksida","D. Helium"],
    "Apa yang dilakukan kampanye kesadaran iklim?": ["A. Menanam pohon di hutan","B. Mengedukasi masyarakat tentang dampak iklim","C. Mengurangi produksi makanan","D. Mempercepat ekstraksi minyak"],
    "Mengapa penting menggunakan produk ramah lingkungan?": ["A. Untuk meningkatkan limbah plastik","B. Untuk melindungi ekosistem dan kesehatan manusia","C. Untuk mengurangi pemanfaatan energi terbarukan","D. Untuk mendapatkan keuntungan cepat"],
    "Bagaimana mekanisme umpan balik albedo dalam pemanasan global?": ["A. Permukaan es yang mencair meningkatkan pantulan matahari","B. Permukaan es yang mencair mengurangi pantulan matahari dan meningkatkan penyerapan panas","C. Pemanasan atmosfer mengurangi jumlah sinar matahari yang sampai bumi","D. Meningkatkan evaporasi akibat udara lebih kering"],
    "Apa peran metana dalam pemanasan global dibandingkan CO2?": ["A. Metana lebih sedikit bahayanya sehingga tidak berkontribusi signifikan","B. Metana memiliki potensial pemanasan global per molekul jauh lebih tinggi meskipun konsentrasinya lebih rendah","C. Metana hanya mempengaruhi ozon stratosfer dan bukan suhu","D. Metana dilepaskan hanya dari kendaraan bermotor"],
    "Bagaimana aerosol sulfat dari aktivitas industri mempengaruhi iklim global?": ["A. Mereka menyerap panas dan meningkatkan pemanasan global","B. Mereka memantulkan sinar matahari dan bersifat pendingin sementara","C. Mereka secara langsung menghasilkan gas rumah kaca","D. Mereka mempercepat pembentukan awan panas"],
    "Mengapa pemanasan laut mempercepat pelelehan es di Greenland?": ["A. Air laut lebih panas mengalir ke bawah es dan meningkatkan pencairan basal","B. Laut yang hangat mengurangi kadar oksigen di atmosfer","C. Laut hangat meningkatkan pembekuan es di permukaan","D. Laut yang hangat hanya berdampak pada cuaca, bukan es"]
}
answers = {
    "Apa itu perubahan iklim?": "B",
    "Apa penyebab utama perubahan iklim?": "D",
    "Apa dampak perubahan iklim?": "A",
    "Bagaimana deforestasi mempengaruhi perubahan iklim?": "A",
    "Manakah sumber energi terbarukan berikut?": "C",
    "Apa yang bisa dilakukan individu untuk menghemat air?": "B",
    "Apa dampak kenaikan permukaan laut?": "A",
    "Mengapa penggunaan kendaraan listrik ramah lingkungan?": "B",
    "Apa fungsi panel surya?": "C",
    "Manakah dari berikut ini yang merupakan gas rumah kaca?": "C",
    "Apa yang dilakukan kampanye kesadaran iklim?": "B",
    "Mengapa penting menggunakan produk ramah lingkungan?": "B",
    "Bagaimana mekanisme umpan balik albedo dalam pemanasan global?": "B",
    "Apa peran metana dalam pemanasan global dibandingkan CO2?": "B",
    "Bagaimana aerosol sulfat dari aktivitas industri mempengaruhi iklim global?": "B",
    "Mengapa pemanasan laut mempercepat pelelehan es di Greenland?": "A"
}
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hai! Saya Bot ClimateChange-EduBot!\nFitur yang tersedia:\n1. $materi - Menampilkan daftar materi perubahan iklim\n2. $quiz - Mengikuti kuis tentang perubahan iklim\n3. $tips - Mendapatkan tips untuk mengurangi dampak perubahan iklim\n4. $resources - Menyediakan sumber daya untuk belajar lebih lanjut tentang perubahan iklim")

@bot.command()
async def materi(ctx):
    await ctx.send("Daftar Materi Perubahan Iklim :\n1. Apa itu Perubahan Iklim? ($materi1)\n2. Penyebab Perubahan Iklim ($materi2)\n3. Dampak Perubahan Iklim ($materi3)\n4. Solusi untuk Mengatasi Perubahan Iklim ($materi4)\n5. Peran Individu dalam Mengatasi Perubahan Iklim ($materi5)\n6. Gas Rumah Kaca dan Efek Rumah Kaca ($materi6)\n7. Energi Terbarukan & Transportasi Ramah Lingkungan ($materi7)\n8. Adaptasi, Kebijakan, dan Aksi Komunitas ($materi8)")

@bot.command()
async def materi1(ctx):
    await ctx.send("Perubahan iklim adalah perubahan jangka panjang dalam pola cuaca global atau regional yang disebabkan oleh aktivitas manusia, seperti pembakaran bahan bakar fosil, deforestasi, dan emisi gas rumah kaca. Perubahan iklim dapat menyebabkan peningkatan suhu global, perubahan pola curah hujan, kenaikan permukaan laut, dan dampak negatif lainnya pada lingkungan dan kehidupan manusia.")

@bot.command()
async def materi2(ctx):
    await ctx.send("Penyebab perubahan iklim utama adalah aktivitas manusia, terutama pembakaran bahan bakar fosil yang menghasilkan emisi gas rumah kaca, deforestasi yang mengurangi penyerapan CO2, dan aktivitas industri yang memproduksi limbah berbahaya.")

@bot.command()
async def materi3(ctx):
    await ctx.send("Dampak perubahan iklim meliputi peningkatan suhu global, perubahan pola cuaca ekstrem, kenaikan permukaan laut, kepunahan spesies, dan dampak negatif pada kesehatan manusia dan ekosistem.")

@bot.command()
async def materi4(ctx):
    await ctx.send("Solusi untuk mengatasi perubahan iklim meliputi pengurangan emisi gas rumah kaca, penggunaan energi terbarukan, penanaman pohon, dan pengembangan teknologi hijau.")

@bot.command()
async def materi5(ctx):
    await ctx.send("Peran individu dalam mengatasi perubahan iklim meliputi pengurangan konsumsi energi, menggunakan transportasi ramah lingkungan, memilih produk ramah lingkungan, dan meningkatkan kesadaran tentang isu perubahan iklim.")

@bot.command()
async def materi6(ctx):
    await ctx.send("Gas rumah kaca seperti karbon dioksida, metana, dan nitrous oxide menyerap panas di atmosfer dan memperkuat efek rumah kaca. Aktivitas manusia, termasuk pembakaran bahan bakar fosil dan peternakan, meningkatkan konsentrasi gas ini. Perubahan reflektivitas Bumi, seperti pencairan es, juga memperburuk pemanasan global melalui umpan balik albedo.")

@bot.command()
async def materi7(ctx):
    await ctx.send("Energi terbarukan seperti tenaga surya, angin, dan air menghasilkan listrik tanpa emisi gas rumah kaca. Transportasi ramah lingkungan termasuk kendaraan listrik, transportasi umum, sepeda, dan jalan kaki. Mengurangi ketergantungan pada bahan bakar fosil membantu menurunkan emisi, polusi, dan memperlambat laju perubahan iklim.")

@bot.command()
async def materi8(ctx):
    await ctx.send("Adaptasi iklim meliputi tindakan untuk mengurangi risiko dampak iklim, seperti sistem drainase yang lebih baik atau varietas tanaman tahan kering. Kebijakan dan aksi komunitas mencakup kampanye kesadaran, dukungan terhadap regulasi lingkungan, dan partisipasi program daur ulang. Peran individu adalah memilih gaya hidup berkelanjutan, memberi suara pada kebijakan hijau, dan mendukung organisasi lingkungan.")

@bot.command()
async def tips(ctx):
    await ctx.send("Tips tentang apa?:\n1. Tips-tips random untuk mengurangi dampak perubahan iklim ($tips1)\n2. Tips-tips random untuk menghemat energi di rumah ($tips2)\n3. Tips-tips random untuk mengurangi penggunaan plastik ($tips3)\n4. Tips-tips random untuk memilih transportasi ramah lingkungan ($tips4)\n5. Tips-tips random untuk mendukung kebijakan perubahan iklim ($tips5)")
@bot.command()
async def tips1(ctx):
    tip = random.choice(Tips1)
    await ctx.send(tip)

@bot.command()
async def tips2(ctx):
    tip = random.choice(Tips2)
    await ctx.send(tip)

@bot.command()
async def tips3(ctx):
    tip = random.choice(Tips3)
    await ctx.send(tip)

@bot.command()
async def tips4(ctx):
    tip = random.choice(Tips4)
    await ctx.send(tip)

@bot.command()
async def tips5(ctx):
    tip = random.choice(Tips5)
    await ctx.send(tip)
@bot.command()
async def resources(ctx):
    await ctx.send("""Sumber Daya untuk Belajar Lebih Lanjut tentang Perubahan Iklim:
1. BMKG – Informasi Iklim Indonesia — Portal utama data, publikasi, dan informasi perubahan iklim Indonesia.
2. BMKG – Klimatologi & Perubahan Iklim — Analisis suhu, curah hujan, dan proyeksi iklim Indonesia.
3. Sekolah Lapang Iklim (BMKG) — Materi literasi iklim untuk masyarakat umum.
4. BMKG – Informasi Gas Rumah Kaca — Data CO₂, CH₄, dan indikator emisi di Indonesia.
5. Direktorat Jenderal Pengendalian Perubahan Iklim (KLHK) — Kebijakan dan program pengendalian perubahan iklim Indonesia.
6. NASA Climate Change — Penjelasan ilmiah, data, dan visualisasi perubahan iklim global.
7. NOAA Climate.gov — Artikel, data, dan edukasi iklim dari pemerintah Amerika Serikat.
8. NOAA National Centers for Environmental Information (NCEI) — Data iklim global dan laporan tahunan kondisi iklim dunia.
""")

@bot.command()
async def quiz(ctx):
    score = 0
    lives = 3
    await ctx.send("Kuis Perubahan Iklim Dimulai! Kamu memiliki 3 nyawa. Jawab pertanyaan berikut dengan benar untuk mendapatkan skor, setiap pertanyaan 30 detik. Salah 3x artinya GAME OVER.")
    remaining = list(questions.keys())
    # loop until no questions left or lives run out
    while lives > 0 and remaining:
        kwestion = random.choice(remaining)
        await ctx.send(f"Pertanyaan: {kwestion}\nPilihan Jawaban:\n" + "\n".join(questions[kwestion]))

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            msg = await bot.wait_for('message', check=check, timeout=30.0)
        except Exception:
            await ctx.send("Waktu habis untuk pertanyaan ini. Nyawa berkurang 1.")
            lives -= 1
            remaining.remove(kwestion)
            continue

        user_answer = msg.content.strip().upper()
        correct = answers.get(kwestion)
        if user_answer == correct:
            score += 1
            await ctx.send(f"Benar! Skor: {score} | Nyawa: {lives}")
        else:
            lives -= 1
            await ctx.send(f"Salah. Jawaban yang benar: {correct}. Skor: {score} | Nyawa: {lives}")

        remaining.remove(kwestion)

    if lives <= 0:
        await ctx.send(f"GAME OVER. Skor akhir: {score}")
    else:
        await ctx.send(f"Kuis selesai! Kamu menjawab semua pertanyaan. Skor akhir: {score}")

@bot.command()
@commands.is_owner() # Restricts command usage strictly to the bot creator
async def shutdown(ctx):
    await ctx.send("Shutting down... Goodbye!")
    await bot.close()

bot.run("YOUR_BOT_TOKEN_HERE")  # Replace with your actual bot token