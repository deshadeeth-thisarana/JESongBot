# Infinity BOTs <https://t.me/Infinity_BOTs>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from JESongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JESongBot import Jebot as app
from JESongBot import LOGGER

pm_start_text = """
Heya [{}](tg://user?id={}), I'm Song Downloader Bot [🎵](https://telegra.ph/file/8fc780bc79ff67d91d1ef.png)

Just send me the song name you want to download.
eg: ```/song Satisfya```

A bot by [Đ€Ş卄ΔĐ€€Ť卄 Ť卄ĪŞΔŘคŇΔ](t.me/DeshadeethThisarana)
"""


@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
             [[
                        InlineKeyboardButton(
                            text="🧰 Support Group 🧰",
                            url="https://t.me/Gangoffriends"),
                         InlineKeyboardButton(
                             text="📺 Update Channel 📺",
                             url="https://t.me/gangoffriendschannel")
                     ],
                     [
                        InlineKeyboardButton(
                            text="➕ Add me to Your Group ↗️",
                            url="https://t.me/Mr_Song_robot?startgroup=start")
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("Song bot is online.")
idle()
