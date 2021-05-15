# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020-2021 by casperteam@Github, < https://github.com/casperteam >.
#
# This file is part of < https://github.com/casperteam/cpbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/casperteam/cpbot/blob/master/LICENSE >
#
# All rights reserved.


class StopConversation(Exception):
    """ raise if conversation has terminated """


class ProcessCanceled(Exception):
    """ raise if thread has terminated """


class cpbotBotNotFound(Exception):
    """ raise if cpbot bot not found """
