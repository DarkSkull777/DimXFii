from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["userbotjoin"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Jadiin gua admin di grup dengan izin penuh biar lu bisa nyuruh gua okey. /help</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "Dimas X Lufi Music"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"Okey gua udah gabung ke grup")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Okeyy gua udah ada di obrolan suara grup</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🔴 BANJIR ERROR 🔴 \nEh elu {user.first_name} gua ga bisa gabung grup elu karena banyak nya permintaan! Pastiin juga gua ga di ban dari grup lu."
                                  "\n\nAtau lu masukin -> @dlaaz ke Grup Ini secara manual terus coba lagi</b>",
        )
        return
    await message.reply_text(
            "<b>Okeyy gua udah gabung ke grup lu</b>",
        )
    
@USER.on_message(filters.group & filters.command(["userbotleave"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>Gua ga bisa left grup Lu!."
            "\n\nAtau Lu kick gua secara manual dari Grup lu</b>",
        )
        return