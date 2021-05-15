# Copyright (C) 2020-2021 by casperteam@Github, < https://github.com/casperteam >.
#
# This file is part of < https://github.com/casperteam/cpbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/casperteam/blob/master/LICENSE >
#
# All rights reserved.

import pyrogram

from main_startup.core.decorators import cpbot_on_cmd
from main_startup.helper_func.basic_helpers import edit_or_reply, edit_or_send_as_file


@cpbot_on_cmd(
    ["listmyusernames"],
    cmd_help={
        "help": "Get All Admin Channel / Chat List",
        "example": "{ch}listmyusernames",
    },
)
async def pabloescobar(client, message):
    pablo = await edit_or_reply(message, "`Please Wait!`")
    channels = await client.send(
        pyrogram.raw.functions.channels.GetAdminedPublicChannels()
    )
    C = channels.chats
    output_stre = ""
    for x in C:
        output_stre += f"{x.title}\n@{x.username}\n\n"
    output_str = f"""I am Admin In All These Groups And Channels
{output_stre}
"""
    await edit_or_send_as_file(
        output_str, pablo, client, "Your Admin Chats", "admin_chat"
    )
