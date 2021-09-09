""" Weebify a text,
Ported from Saitama Bot. 
By :- @PhycoNinja13b
Modified by :- @kirito6969
.weeb <text> """

from userbot.utils import admin_cmd

normiefont = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
]

weebyfont = [
    "a",
    "ɮ",
    "ƈ",
    "ɖ",
    "ɛ",
    "ʄ",
    "ɢ",
    "ɦ",
    "ɨ",
    "ʝ",
    "ӄ",
    "ʟ",
    "ʍ",
    "ռ",
    "օ",
    "ք",
    "զ",
    "ʀ",
    "ֆ",
    "ȶ",
    "ʊ",
    "ʋ",
    "ա",
    "Ӽ",
    "ʏ",
    "ʐ",
]
lol = [
    "𝔸",
    "𝔹",
    "ℂ",
    "𝔻",
    "𝔼",
    "𝔽",
    "𝔾",
    "ℍ",
    "𝕀",
    "𝕁",
    "𝕂",
    "𝕃",
    "𝕄",
    "ℕ",
    "𝕆",
    "ℙ",
    "ℚ",
    "ℝ",
    "𝕊",
    "𝕋",
    "𝕌",
    "𝕍",
    "𝕎",
    "𝕏",
    "𝕐",
    "ℤ",
]

hell = [
    "ᴀ",
    "ʙ",
    "ᴄ",
    "ᴅ",
    "ᴇ",
    "ꜰ",
    "ɢ",
    "ʜ",
    "ɪ",
    "ᴊ",
    "ᴋ",
    "ʟ",
    "ᴍ",
    "ɴ",
    "ᴏ",
    "ᴘ",
    "Q",
    "ʀ",
    "ꜱ",
    "ᴛ",
    "ᴜ",
    "ᴠ",
    "ᴡ",
    "c",
    "x",
    "ʏ",
    "ᴢ",
]

weebified = [
    "🅰",
    "🅱",
    "🅲",
    "🅳",
    "🅴",
    "🅵",
    "🅶",
    "🅷",
    "🅸",
    "🅹",
    "🅺",
    "🅻",
    "🅼",
    "🅽",
    "🅾",
    "🅿",
    "🆀",
    "🆁",
    "🆂",
    "🆃",
    "🆄",
    "🆅",
    "🆆",
    "🆇",
    "🆈",
    "🆉",
]

weebifin = [
    "🇦‌",
    "🇧‌",
    "🇨‌",
    "🇩‌",
    "🇪‌",
    "🇫‌",
    "🇬‌",
    "🇭‌",
    "🇮‌",
    "🇯‌",
    "🇰‌",
    "🇱‌",
    "🇲‌",
    "🇳‌",
    "🇴‌",
    "🇵‌",
    "🇶‌",
    "🇷‌",
    "🇸‌",
    "🇹‌",
    "🇺‌",
    "🇻‌",
    "🇼‌",
    "🇽‌",
    "🇾‌",
    "🇿‌",
]

weebed = [
    "ᴬ",
    "ᴮ",
    "ᶜ",
    "ᴰ",
    "ᴱ",
    "ᶠ",
    "ᴳ",
    "ᴴ",
    "ᴵ",
    "ᴶ",
    "ᴷ," "ᴸ",
    "ᴹ",
    "ᴺ",
    "ᴼ",
    "ᴾ",
    "Q",
    "ᴿ",
    "ˢ",
    "ᵀ",
    "ᵁ",
    "ⱽ",
    "ᵂ",
    "ˣ",
    "ʸ",
    "ᶻ",
]

weebid = [
    "ꋫ",
    "ꃃ",
    "ꏸ",
    "ꁕ",
    "ꍟ",
    "ꄘ",
    "ꁍ",
    "ꑛ",
    "ꂑ",
    "ꀭ",
    "ꀗ",
    "꒒",
    "ꁒ",
    "ꁹ",
    "ꆂ",
    "ꉣ",
    "ꁸ",
    "꒓",
    "ꌚ",
    "꓅",
    "ꐇ",
    "ꏝ",
    "ꅐ",
    "ꇓ",
    "ꐟ",
    "ꁴ",
]

weebus = [
    "ɐ",
    "q",
    "ɔ",
    "p",
    "ǝ",
    "ɟ",
    "ƃ",
    "ɥ",
    "ᴉ",
    "ɾ",
    "ʞ",
    "l",
    "ɯ",
    "u",
    "o",
    "d",
    "b",
    "ɹ",
    "s",
    "ʇ",
    "n",
    "ʌ",
    "ʍ",
    "x",
    "ʎ",
    "z",
]

webbind = [
    "α",
    "ɓ",
    "૮",
    "∂",
    "ε",
    "ƒ",
    "ɠ",
    "ɦ",
    "เ",
    "ʝ",
    "ҡ",
    "ℓ",
    "ɱ",
    "ɳ",
    "σ",
    "ρ",
    "φ",
    "૨",
    "ร",
    "ƭ",
    "µ",
    "ѵ",
    "ω",
    "א",
    "ყ",
    "ƶ",
]

ucker = [
    "𝒶",
    "𝒷",
    "𝒸",
    "𝒹",
    "𝑒",
    "𝒻",
    "𝑔",
    "𝒽",
    "𝒾",
    "𝒿",
    "𝓀",
    "𝓁",
    "𝓂",
    "𝓃",
    "𝑜",
    "𝓅",
    "𝓆",
    "𝓇",
    "𝓈",
    "𝓉",
    "𝓊",
    "𝓋",
    "𝓌",
    "𝓍",
    "𝓎",
    "𝓏",
]

gouse = [
    "ą",
    "ɓ",
    "ƈ",
    "ɗ",
    "ҽ",
    "ƒ",
    "ɠ",
    "ɦ",
    "í",
    "ᴊ",
    "ƙ",
    "Ɩ",
    "ɱ",
    "ղ",
    "օ",
    "ƥ",
    "ʠ",
    "ɾ",
    "ʂ",
    "ƭ",
    "ʋ",
    "ⱱ",
    "ⱳ",
    "x",
    "ყ",
    "z",
]

rexmodz = [
    "A͎",
    "B͎",
    "C͎",
    "D͎",
    "E͎",
    "F͎",
    "G͎",
    "H͎",
    "I͎",
    "J͎",
    "K͎",
    "L͎",
    "M͎",
    "N͎",
    "O͎",
    "P͎",
    "Q͎",
    "R͎",
    "S͎",
    "T͎",
    "U͎",
    "V͎",
    "W͎",
    "X͎",
    "Y͎",
    "Z͎",
]

legend = ["1͎", "2͎", "3͎", "4͎", "5͎", "6͎", "7͎", "8͎", "9͎", "0͎"]

me = [
    "ᗩ",
    "ᙖ",
    "ᙅ",
    "ᗪ",
    "ᙓ",
    "ᖴ",
    "ᘜ",
    "ᕼ",
    "I",
    "ᒍ",
    "K",
    "ᒪ",
    "ᙏ",
    "ᑎ",
    "O",
    "ᑭ",
    "ᑫ",
    "ᖇ",
    "S",
    "T",
    "ᙀ",
    "ᐯ",
    "ᙎ",
    "᙭" "Y" "ᘔ",
]


@bot.on(admin_cmd(pattern="f1 ?(.*)"))
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`What I am Supposed to Weebify U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await event.edit(string)


@bot.on(admin_cmd(pattern="f2 ?(.*)"))
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`What I am Supposed to Weebify U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = lol[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await event.edit(string)


@bot.on(admin_cmd(pattern="f3 ?(.*)"))
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`What I am Supposed to Weebify U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = hell[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await event.edit(string)


@bot.on(admin_cmd(pattern="f4 ?(.*)"))
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`What I am Supposed to Weebify U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebified[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await event.edit(string)


@bot.on(admin_cmd(pattern="f5 ?(.*)"))
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`What I am Supposed to Weebify U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebifin[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await event.edit(string)


@bot.on(admin_cmd(pattern="f6 ?(.*)"))
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`What I am Supposed to Weebify U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = webbid[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await event.edit(string)


@bot.on(admin_cmd(pattern="f0 ?(.*)"))
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`What I am Supposed to Weebify U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = ucker[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await event.edit(string)


@bot.on(admin_cmd(pattern="fa ?(.*)"))
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`What I am Supposed to Weebify U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = rexmodz[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await event.edit(string)


@bot.on(admin_cmd(pattern="n1 ?(.*)"))
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`What I am Supposed to Weebify U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = legend[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await event.edit(string)


@bot.on(admin_cmd(pattern="fb ?(.*)"))
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`What I am Supposed to Weebify U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = gouse[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await event.edit(string)


@bot.on(admin_cmd(pattern="fc ?(.*)"))
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`What I am Supposed to Weebify U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = me[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await event.edit(string)


@bot.on(admin_cmd(pattern="f7 ?(.*)"))
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`What I am Supposed to Weebify U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebed[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await event.edit(string)


@bot.on(admin_cmd(pattern="f8 ?(.*)"))
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`What I am Supposed to Weebify U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebus[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await event.edit(string)


@bot.on(admin_cmd(pattern="f9 ?(.*)"))
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`What I am Supposed to Weebify U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = webbind[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await event.edit(string)
