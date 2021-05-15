# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020-2021 by casperteam@Github, < https://github.com/casperteam >.
#
# This file is part of < https://github.com/casperteam/cpbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/casperteam/cpbot/blob/master/LICENSE >
#
# All rights reserved.

__all__ = ['GetLogger']

import inspect

from cpbot import logging

_LOG = logging.getLogger(__name__)
_LOG_STR = "<<<!  #####  %s  #####  !>>>"


class GetLogger:  # pylint: disable=missing-class-docstring
    @staticmethod
    def getLogger(name: str = '') -> logging.Logger:  # pylint: disable=invalid-name
        """ This returns new logger object """
        if not name:
            name = inspect.currentframe().f_back.f_globals['__name__']
        _LOG.debug(_LOG_STR, f"Creating Logger => {name}")
        return logging.getLogger(name)
