from userbot.Config import Config
import asyncio

import requests
from telethon import functions

from userbot import ALIVE_NAME, CMD_LIST, SUDO_LIST
from LEGENDBOT.utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern="op ?(.*)", outgoing=True))
async def yardim(event):
    if event.fwd_from:
        return
    tgbotusername = Config.BOT_USERNAME
    input_str = event.pattern_match.group(1)
    if tgbotusername is not None or LEGEND_input == "text":
        results = await event.client.inline_query(tgbotusername, "@LEGEND_Userbot")
        await results[0].click(
            event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
        )
        await event.delete()
    else:
        await edit_or_reply(event, ["NO_BOT"])
    
        if input_str in CMD_LIST:
          string = "Commands found in {}:\n".format(input_str)
          for i in CMD_LIST[input_str]:
              string += "  " + i
              string += "\n"
          await event.edit(string)
        else:
          await event.edit(input_str + " is not a valid plugin!")


@bot.on(sudo_cmd(allow_sudo=True, pattern="op ?(.*)"))
async def info(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "text":
        string = (
            "♦️Total {count} commands found in {plugincount} sudo plugins of  𝖑𝖊ɠêɳ̃dẞø✞︎\n\n"
        )
        LEGENDcount = 0
        plugincount = 0
        for i in sorted(SUDO_LIST):
            plugincount += 1
            string += f"{plugincount}) Commands found in Plugin " + i + " are \n"
            for iter_list in SUDO_LIST[i]:
                string += "    " + str(iter_list)
                string += "\n"
                LEGENDcount += 1
            string += "\n"
        if len(string) > 4095:
            data = string.format(count=LEGENDcount, plugincount=plugincount)
            key = (
                requests.post(
                    "https://nekobin.com/api/documents", json={"content": data}
                )
                .json()
                .get("result")
                .get("key")
            )
            url = f"https://nekobin.com/{key}"
            reply_text = f"All commands of the LEGENDBOT are [here]({url})"
            await event.reply(reply_text, link_preview=False)
            return
        await event.reply(
            string.format(count=LEGENDcount, plugincount=plugincount), link_preview=False
        )
        return
    if input_str:
        if input_str in SUDO_LIST:
            string = "<b>{count} Commands found in plugin {input_str}:</b>\n\n"
            LEGENDcount = 0
            for i in SUDO_LIST[input_str]:
                string += f"  •  <code>{i}</code>"
                string += "\n"
                LEGENDcount += 1
            await event.reply(
                string.format(count=LEGENDcount, input_str=input_str), parse_mode="HTML"
            )
        else:
            reply = await event.reply(input_str + " is not a valid plugin!")
            await asyncio.sleep(3)
            await event.delete()
            await reply.delete()
    else:
        string = "<b>Please specify which plugin do you want help for !!\
            \nNumber of plugins : </b><code>{count}</code>\
            \n<b>Usage:</b> <code>.op plugin name</code>\n\n"
        LEGENDcount = 0
        for i in sorted(SUDO_LIST):
            string += "≈ " + f"<code>{str(i)}</code>"
            string += " "
            LEGENDcount += 1
        await event.reply(string.format(count=LEGENDcount), parse_mode="HTML")
