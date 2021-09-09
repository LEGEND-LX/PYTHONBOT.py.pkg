"""Restart or Terminate the bot from any chat
Available Commands:
.restart
.shutdown
.reboot"""
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html
from telethon import events
import asyncio
import os
import sys
from userbot.utils import admin_cmd, sudo_cmd


@bot.on(admin_cmd(pattern="restart"))
@bot.on(sudo_cmd(pattern="restart"))
async def _(event):
    await event.edit("Restarting ▰▱▱▱▱▱▱▱18%...")
    await asyncio.sleep(1)
    await event.edit("Restarting ▰▰▰▰▱▱▱▱49.6%...")
    await asyncio.sleep(1)
    await event.edit("Restarting ▰▰▰▰▰▰▰▰100%...")
    await asyncio.sleep(0.1)
    await event.edit("Restarted boss....✈ `.king` me or type `.help` or type '.awake' or type '.allive' to check if your Du is online/alive ")
    await bot.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()


@bot.on(admin_cmd(pattern="shutdown"))
@bot.on(sudo_cmd(pattern="shutdown"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Turning dyno off ...Manually turn me on later")
    await bot.disconnect()

@bot.on(events.NewMessage(pattern=r"\.reboot", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    
    await event.edit("╭━━━╮\n┃╭━╮┃\n┃╰━━┳━━┳━┳╮╭┳━━┳━╮\n╰━━╮┃┃━┫╭┫╰╯┃┃━┫╭╯\n┃╰━╯┃┃━┫┃╰╮╭┫┃━┫┃\n╰━━━┻━━┻╯╱╰╯╰━━┻╯\n╭━━━╮╱╱╱╱╱╭╮╱╱╱╱╱╭╮\n┃╭━╮┃╱╱╱╱╭╯╰╮╱╱╱╭╯╰╮\n┃╰━╯┣━━┳━┻╮╭╋━━┳┻╮╭╋┳━╮╭━━╮\n┃╭╮╭┫┃━┫━━┫┃┃╭╮┃╭┫┃┣┫╭╮┫╭╮┃\n┃┃┃╰┫┃━╋━━┃╰┫╭╮┃┃┃╰┫┃┃┃┃╰╯┣┳┳╮\n╰╯╰━┻━━┻━━┻━┻╯╰┻╯╰━┻┻╯╰┻━╮┣┻┻╯\n╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃\n╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯")
    await asyncio.sleep(2)
    await event.edit("╭━━━╮\n┃╭━╮┃\n┃╰━━┳━━┳━┳╮╭┳━━┳━╮\n╰━━╮┃┃━┫╭┫╰╯┃┃━┫╭╯\n┃╰━╯┃┃━┫┃╰╮╭┫┃━┫┃\n╰━━━┻━━┻╯╱╰╯╰━━┻╯\n╭━━━╮╱╱╱╱╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╭╮\n┃╭━╮┃╱╱╱╱╭╯╰╮╱╱╱╭╯╰╮╱╱╱╱┃┃\n┃╰━╯┣━━┳━┻╮╭╋━━┳┻╮╭╋━━┳━╯┃\n┃╭╮╭┫┃━┫━━┫┃┃╭╮┃╭┫┃┃┃━┫╭╮┃j\n┃┃┃╰┫┃━╋━━┃╰┫╭╮┃┃┃╰┫┃━┫╰╯┣╮\n╰╯╰━┻━━┻━━┻━┻╯╰┻╯╰━┻━━┻━━┻╯")
    await asyncio.sleep(0.1)
    await event.edit("🇸 🇪 🇷 🇻 🇪 🇷  🇷 🇪 🇧 🇴 🇴 🇹 🇪 🇩  = ✅")
    await bot.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
