##
# Copyright (c) 2010 Sprymix Inc.
# All rights reserved.
#
# See LICENSE for details.
##


import ctypes
import atexit

from .wrapper_base import *
from . import _magickwand as api
from ._magickwand import *


api.MagickWandGenesis()
atexit.register(api.MagickWandTerminus)


class MagickWandError(Exception): pass


class IMWrapper(CTypeWrapper):
    def _check_error(self):
        severity = api.ExceptionType()
        description = api.MagickGetException(self, severity)
        raise MagickWandError(description)


class MagickWand(IMWrapper):
    _ctype = api.MagickWand

    def _create(self):
        return api.NewMagickWand()

    def _clone(self):
        return api.CloneMagickWand(self)

    def _destroy(self):
        return api.DestroyMagickWand(self)

adapt_module(api)
