from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hola:V, Ini adalah layanan bot musik.\n\n ❗️ Rules:\n   - ga ada mengobrol yang diizinkan\n   - ga ada spam yang diizinkan \n\n 👉 **KIRIM LINK UNDANGAN GRUP ATAU NAMA PENGGUNA JIKA USERBOT TIDAK DAPAT BERGABUNG DENGAN GRUP ANDA.**\n\n ⚠️ Peringatan: Jika Anda mengirim pesan di sini berarti admin akan melihat pesan Anda dan bergabung dengan obrolan\n    - Jangan tambahkan pengguna ini ke grup rahasia.\n   - Jangan Bagikan info pribadi di sini\n\n")
  return                        