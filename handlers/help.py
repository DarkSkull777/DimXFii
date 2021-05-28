from pyrogram import Client, filters
from pyrogram.types import Message



@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""🔥 Semua perintah untuk menjalankan bot!
**Perintah Untuk Member**
- `/play <Judul Lagu>` - Putar Lagu Yang Lu Mau
- `/dplay <Judul Lagu>` - Putar Lagu Yang Lu Mau Dari Deezer
- `/splay <Judul Lagu>` - Putar Lagu Yang Lu Mau Dari Saavn
- `/playlist` - Ngintip isi playlist
- `/current` - Ngeliat Lagu Yang Lagi Di Putar
- `/song <Judul Lagu>` - Download Lagu Yang Lu Mau dengan cepat
- `/search <query>` - Cari Video Di YouTube Dengan Detail
- `/deezer <Judul Lagu>` - Download Lagu Yang Lu Mau Dengan Cepat Pake Via Deezer
- `/saavn <Judul Lagu>` - Download Lagu Yang Lu Mau Dengan Cepat Melalui Dengan Via Saavn
- `/video <Judul Lagu>` - Download Video Yang Lu Mau Dengan Cepat

**Admins only**
- `/player` - Buka Panel Pengaturan Pemutar Musik
- `/pause` - Berhentiin Lagu Yang Lagi Di Putar
- `/resume` - Ngelanjutin Lagu Yang Tadi Elu Pause
- `/skip` - Lu Ganti Ke Lagu Yang Berikutnya
- `/end` - Berhenti Untuk Musik Nya
- `/userbotjoin` - Menyuruh Join Ke Obrolan Suara
- `/userbotleave` - Keluarin User Pemutaran Musik
- `/admincache` - Refresh Daftar Admin""")

@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""🔥 Semua perintah untuk menjalankan bot!
**Perintah Untuk Member**
- `/play <Judul Lagu>` - Putar Lagu Yang Lu Mau
- `/dplay <Judul Lagu>` - Putar Lagu Yang Lu Mau Dari Deezer
- `/splay <Judul Lagu>` - Putar Lagu Yang Lu Mau Dari Saavn
- `/playlist` - Ngintip isi playlist
- `/current` - Ngeliat Lagu Yang Lagi Di Putar
- `/song <Judul Lagu>` - Download Lagu Yang Lu Mau dengan cepat
- `/search <query>` - Cari Video Di YouTube Dengan Detail
- `/deezer <Judul Lagu>` - Download Lagu Yang Lu Mau Dengan Cepat Pake Via Deezer
- `/saavn <Judul Lagu>` - Download Lagu Yang Lu Mau Dengan Cepat Melalui Dengan Via Saavn
- `/video <Judul Lagu>` - Download Video Yang Lu Mau Dengan Cepat

**Admins only**
- `/player` - Buka Panel Pengaturan Pemutar Musik
- `/pause` - Berhentiin Lagu Yang Lagi Di Putar
- `/resume` - Ngelanjutin Lagu Yang Tadi Elu Pause
- `/skip` - Lu Ganti Ke Lagu Yang Berikutnya
- `/end` - Berhenti Untuk Musik Nya
- `/userbotjoin` - Menyuruh Join Ke Obrolan Suara
- `/userbotleave` - Keluarin User Pemutaran Musik
- `/admincache` - Refresh Daftar Admin""")