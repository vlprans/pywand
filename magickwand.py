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


class IMWrapperMeta(CTypeWrapperMeta):
    def __new__(mcs, name, bases, dct):
        _im_new = dct.get('_im_new', None)
        _im_clone = dct.get('_im_clone', None)
        _im_destroy = dct.get('_im_destroy', None)
        _im_get_exception = dct.get('_im_get_exception', None)

        if _im_new:
            dct['_create'] = lambda self: _im_new()
        if _im_clone:
            dct['_clone'] = lambda self: _im_clone(self)
        if _im_destroy:
            dct['_destroy'] = lambda self: _im_destroy(self)
        if _im_get_exception:
            def _throw_error(self):
                severity = api.ExceptionType()
                description = _im_get_exception(self, severity)
                raise MagickWandError(description)

            dct['_throw_error'] = _throw_error

        return super().__new__(mcs, name, bases, dct)


class IMWrapper(CTypeWrapper, metaclass=IMWrapperMeta): pass


class MagickWand(IMWrapper):
    _ctype = api.MagickWand
    _im_new = api.NewMagickWand
    _im_clone = api.CloneMagickWand
    _im_get_exception = api.MagickGetException


adapt_module(api)
