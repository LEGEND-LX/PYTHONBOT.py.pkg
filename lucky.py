# plugin by lejend @hellboi_atul
"""Emoji

Available Commands:

.lucky"""

from telethon import events

import asyncio
from userbot.utils import admin_cmd




@bot.on(admin_cmd(pattern="lucky"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 17)

    #input_str = event.pattern_match.group(1)

    #if input_str == "lucky":

    await event.edit("Lucky...š¤š¤")

    animation_chars = [
        
            "ā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬[š](/hellboi-atul/hellboi-atul)ā¬",
            "ā¬ā¬ā¬ā¬ā¬\nšā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬[š](/hellboi-atul/hellboi-atul)ā¬",
            "ā¬ā¬ā¬ā¬ā¬\nā¬šā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬[š](/hellboi-atul/hellboi-atul)ā¬",
            "ā¬ā¬ā¬ā¬ā¬\nā¬ā¬šā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬[š](/hellboi-atul/hellboi-atul)ā¬",
            "ā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬šā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬[š](/hellboi-atul/hellboi-atul)ā¬",    
            "ā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬šā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬[š](/hellboi-atul/hellboi-atul)ā¬",
            "ā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬šā¬\nā¬ā¬ā¬[š](/hellboi-atul/hellboi-atul)ā¬",
            "ā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬šā¬\nā¬ā¬ā¬[š](/hellboi-atul/hellboi-atul)ā¬\nā¬ā¬ā¬ā¬ā¬",
            "ā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬šā¬\nā¬ā¬ā¬[š](/hellboi-atul/hellboi-atul)ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬",
            "ā¬ā¬ā¬ā¬ā¬\nā¬ā¬šā¬ā¬\nā¬ā¬[š](/hellboi-atul/hellboi-atul)ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬",
            "ā¬ā¬ā¬ā¬ā¬\nā¬šā¬ā¬ā¬\nā¬[š](/hellboi-atul/hellboi-atul)ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬",
            "ā¬ā¬ā¬ā¬ā¬\nšā¬ā¬ā¬ā¬\n[š](/hellboi-atul/hellboi-atul)ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬",
            "ā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬",
            "ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬",
            "ā¬ā¬ā¬\nā¬ā¬ā¬\nā¬ā¬ā¬",
            "ā¬ā¬\nā¬ā¬",
            "[ššš»Ye le gift](/hellboi-atul/hellboi-atul)"

 ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 17])
