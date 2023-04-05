import psutil

from time import time

from telegram.utils.helpers import escape_markdown

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from handlers import StartTime
from helpers.filters import command
from config import SUPPORT_GROUP, PING_IMG, BOT_NAME


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time


@Client.on_message(command(["ping", "repo", "axen", "alive"]) & filters.group & ~filters.edited)
async def ping(_, message: Message):
    start = time()
    bot_uptime = escape_markdown(get_readable_time((time() - StartTime)))
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    end = time()
    resp = end - start
    await message.reply_photo(
        photo=PING_IMG,
        caption=f"<b> ᴩᴏɴɢ ! </b>\n 🏓 {resp} ᴍs\n\n<b><u>{BOT_NAME} sʏsᴛᴇᴍ sᴛᴀᴛs:</u></b>\n\n• ᴜᴩᴛɪᴍᴇ : {bot_uptime}\n• ᴄᴩᴜ : {cpu}%\n• ᴅɪsᴋ : {disk}%\n• ʀᴀᴍ : {mem}",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GROUP}"),
                    InlineKeyboardButton("sᴏᴜʀᴄᴇ", url=f"https://t.me/NightHighs")
                ]
            ]
        )
    )
    await message.delete()  # delete the original command message
