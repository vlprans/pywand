##
# Copyright (c) 2010 Sprymix Inc.
# All rights reserved.
#
# See LICENSE for details.
##


import ctypes


__all__ = ['CTypeWrapperMeta', 'CTypeWrapper',
           'get_ctype_wrapper', 'adapt_ctype', 'adapt_cfunc', 'adapt_module']


class CTypeWrapperMeta(type):
    types = {}

    def __new__(mcs, name, bases, dct):
        cls = super().__new__(mcs, name, bases, dct)
        if '_ctype' in dct:
            ctype = dct['_ctype']
            mcs.types[ctype] = cls
        return cls

    @classmethod
    def get_ctype_wrapper(mcs, ctype):
        if ctype in mcs.types:
            wrapper = mcs.types[ctype]
        elif issubclass(ctype, ctypes._Pointer) and ctype._type_ in mcs.types:
            wrapper = mcs.types[ctype._type_]
        elif ctypes.POINTER(ctype) in mcs.types:
            wrapper = mcs.types[ctypes.POINTER(ctype)]
        else:
            raise ValueError('No wrapper available for ctype %s' % ctype)
        return wrapper

    @classmethod
    def adapt_ctype(mcs, ctype):
        wrapper = ctype
        try:
            wrapper = mcs.get_ctype_wrapper(ctype)
        except ValueError: pass
        return wrapper

    @classmethod
    def adapt_cfunc(mcs, func):
        if not isinstance(func, ctypes._CFuncPtr):
            raise TypeError('expected ctypes FuncPtr')
        if func.restype is not None:
            func.restype = mcs.adapt_ctype(func.restype)
        func.argtypes = [mcs.adapt_ctype(t) for t in func.argtypes]
        return func

    @classmethod
    def adapt_module(mcs, module):
        for name in module.__all__ if hasattr(module, '__all__') else dir(module):
            func = getattr(module, name)
            if isinstance(func, ctypes._CFuncPtr):
                adapt_cfunc(func)


get_ctype_wrapper = CTypeWrapperMeta.get_ctype_wrapper
adapt_ctype = CTypeWrapperMeta.adapt_ctype
adapt_cfunc = CTypeWrapperMeta.adapt_cfunc
adapt_module = CTypeWrapperMeta.adapt_module


class CTypeWrapper(metaclass=CTypeWrapperMeta):
    def __init__(self, obj = None):
        if obj is not None:
            if isinstance(obj, (self.ctype, self.ctype_ptr)):
                self._obj = obj
            elif isinstance(obj, int):
                self._obj = ctypes.cast(obj, self.ctype_ptr)
            else:
                raise TypeError('expected %s instance or pointer, got %s' % (self.ctype.__name__,
                                                                             obj))
        elif hasattr(self, '_create'):
            self._obj = self._create()
        else:
            self._obj = None

    def __del__(self):
        if hasattr(self, '_destroy') and self._obj:
            #self._destroy() # XXX
            self._obj = None

    def __copy__(self):
        if hasattr(self, '_clone'):
            res =  self._clone()
        else:
            res = type(self)(self._obj)
        return res

    @property
    def ctype(cls):
        return cls._ctype

    @property
    def ctype_ptr(cls):
        return ctypes.POINTER(cls._ctype)

    @property
    def _as_parameter_(self):
        return self._obj

    @classmethod
    def from_param(cls, val):
        if isinstance(val, cls):
            res = val
        else:
            res = cls(val)
        return res
