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
            def throw_error(self):
                severity = api.ExceptionType()
                description = _im_get_exception(self, severity)
                raise MagickWandError(description.decode())

            dct['throw_error'] = throw_error

        return super().__new__(mcs, name, bases, dct)


class IMWrapper(CTypeWrapper, metaclass=IMWrapperMeta): pass


class MagickWand(IMWrapper):
    _ctype = api.MagickWand
    _im_new = api.NewMagickWand
    _im_clone = api.CloneMagickWand
    _im_destroy = api.DestroyMagickWand
    _im_get_exception = api.MagickGetException


class PixelWand(IMWrapper):
    _ctype = api.PixelWand
    _im_new = api.NewPixelWand
    _im_clone = api.ClonePixelWand
    _im_destroy = api.DestroyPixelWand
    _im_get_exception = api.PixelGetException


class DrawingWand(IMWrapper):
    _ctype = api.DrawingWand
    _im_new = api.NewDrawingWand
    _im_clone = api.CloneDrawingWand
    _im_destroy = api.DestroyDrawingWand
    _im_get_exception = api.DrawGetException


class Image(IMWrapper):
    _ctype = api.Image


class PixelIterator(IMWrapper):
    _ctype = api.PixelIterator
    _im_destroy = api.DestroyPixelIterator
    _im_clone = api.ClonePixelIterator
    _im_get_exception = api.PixelIteratorGetException


class Hashmap(IMWrapper):
    _ctype = api.HashmapInfo
    _im_destroy = api.DestroyHashmap


class LinkedList(IMWrapper):
    _ctype = api.LinkedListInfo
    _im_destroy = api.DestroyLinkedList


class SplayTree(IMWrapper):
    _ctype = api.SplayTreeInfo
    _im_destroy = api.DestroySplayTree


class XMLTree(IMWrapper):
    _ctype = api.XMLTreeInfo
    _im_destroy = api.DestroyXMLTree


adapt_module(api)
