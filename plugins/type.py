# Copyright (C) 2020-2021 by casperteam@Github, < https://github.com/casperteam >.
#
# This file is part of < https://github.com/casperteam/cpbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/casperteam/cpbot/blob/master/LICENSE >
#
# All rights reserved.

from cpbot import cpbot, Message


@cpbot.on_cmd("type", about={
    'header': "Simulate a typewriter",
    'usage': "{tr}type [text]"})
async def type_(message: Message):
    text = message.input_str
    if not text:
        await message.err("input not found")
        return
    typing_symbol = '|'
    old_text = ''
    await message.edit(typing_symbol)
    for character in text:
        if message.process_is_canceled:
            await message.edit("`process cancelled`")
            break
        old_text += character
        typing_text = old_text + typing_symbol
        await message.try_to_edit(typing_text, sudo=False)
        await message.try_to_edit(old_text, sudo=False)
