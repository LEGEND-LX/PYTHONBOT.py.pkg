# Thanks to @PYTHON_CODER_SRINIVAS.. 
# animation Idea by @PYTHON_CODER_SRINIVAS
# Made by @PYTHON_CODER_SRINIVAS...and thanks to @PYTHON_CODER_SRINIVAS...the logos...
# Kang with credits else gay...
import asyncio
import random
from telethon import events
from LEGENDBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
# π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND BOT"

# Thanks to ASHUTOSH BRO.. 
# animation Idea by @PYTHON_CODER_SRINIVAS (op coder)
# Made by @PYTHON_CODER_SRINIVAS...and thanks to @koi_nhi_apna for the logos...
# Kang with credits else gay...
# alive.py for ΙΗΚΣ ΦΙ¦ΗΙΦΥ‘

edit_time = 5
""" =======================CONSTANTS====================== """
file1="https://telegra.ph/file/506a27d3c3c70a7cc2833.jpg"
file2="https://telegra.ph/file/c654d129dece33caae44a.jpg"
file3="https://telegra.ph/file/ecdd9d1b3982292813352.jpg"
file4="https://telegra.ph/file/1fc370c843a84c532d420.jpg"""" =======================CONSTANTS====================== """
pm_caption = "Pikachu loverπΙ¨Φ ΦΥΌΚΙ¨ΥΌΙ..!! **π₯π₯\n\n"
pm_caption += "βοΈβοΈ **Master, Am Alive And Systems Are Working Perfectly As It Should Be...**βοΈβοΈ\n\n"
pm_caption += "ΰΌΰΌβ οΈοΈAbout My System \n\n"
pm_caption += "π₯π₯ **α΄α΄Κα΄α΄Κα΄Ι΄**π₯π₯ >>γ 15.0.0\n"
pm_caption += "π¨π¨ **group**π¨π¨   >>γ [ΚΦΙ¨ΥΌ](https://t.me/bothelpcommamds)\n"
pm_caption += f"π°π°**α΄α΄sα΄α΄Κ**π°π°  >>γ {DEFAULTUSER}\n"
pm_caption += "ππ **α΄Κα΄α΄α΄α΄Κ**ππ  >>γ [α΄α΄‘Ι΄α΄Κ](https://t.me/pikachulover1st)\n\n"
pm_caption += "πΆπΆ **α΄Κα΄α΄Ιͺα΄s**πΆπΆ  >>γ [ΚΚα΄](https://t.me/devil_killer1st)\n\n"
pm_caption += "[....βββββββββ\n....βββββββββ\n.......βββββββ\n...............βββ\n](https://t.me/bothelpcommamds)\n\n"
@bot.on(admin_cmd(pattern=r"alive"))

async def amireallyalive(yes):
    chat = await yes.get_chat()

    on = await bot.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(yes.chat_id, ok6, file=file4)

    await alive.delete()
    
    """ For .alive command, check if the bot is running.  """
    await bot.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()