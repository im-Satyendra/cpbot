""" convert text """

# Copyright (C) 2020-2021 by casperteam@Github, < https://github.com/casperteam >.
#
# This file is part of < https://github.com/casperteam/cpbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/casperteam/cpbot/blob/master/LICENSE >
#
# All rights reserved.

from cpbot import cpbot, Message


@cpbot.on_cmd("small", about={
    'header': "Make caps smaller",
    'usage': "{tr}small [text | reply to msg]"})
async def small_(message: Message):
    """ text to small """
    text = message.input_str
    if message.reply_to_message:
        text = message.reply_to_message.text
    if not text:
        await message.err("input not found")
        return
    await message.edit(text.translate(str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                                    "ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘqʀꜱᴛᴜᴠᴡxʏᴢ")))


@cpbot.on_cmd("lower", about={
    'header': "Convert text to lowwer",
    'usage': "{tr}lower [text | reply to msg]"})
async def lower_(message: Message):
    """ text to lower """
    text = message.input_str
    if message.reply_to_message:
        text = message.reply_to_message.text
    if not text:
        await message.err("input not found")
        return
    await message.edit(text.lower())


@cpbot.on_cmd("upper", about={
    'header': "Convert text to upper",
    'usage': "{tr}upper [text | reply to msg]"})
async def upper_(message: Message):
    """ text to upper """
    text = message.input_str
    if message.reply_to_message:
        text = message.reply_to_message.text
    if not text:
        await message.err("input not found")
        return
    await message.edit(text.upper())
