#!/usr/bin/python2

##
# Copyright (c) 2010 Sprymix Inc.
# All rights reserved.
#
# See LICENSE for details.
##

##
# This script is Py2k-only because ctypeslib is not available for Py3k.
##

import sys
import os.path
import subprocess
import ctypes.util
import ctypeslib.codegen.codegenerator
from ctypeslib import xml2py, h2xml


class IMGenerator(ctypeslib.codegen.codegenerator.Generator):
    def get_sharedlib(self, dllname, cc):
        if cc == "stdcall":
            self.need_WinLibraries()
            if not dllname in self._stdcall_libraries:
                print >> self.imports, "_stdcall_libraries[%r] = WinDLL(%r)" % (dllname, dllname)
                self._stdcall_libraries[dllname] = None
            return "_stdcall_libraries[%r]" % dllname
        self.need_CLibraries()
        if self.preloaded_dlls != []:
          global_flag = ", mode=RTLD_GLOBAL"
        else:
          global_flag = ""
        if not dllname in self._c_libraries:
            print >> self.imports, "from ctypes.util import find_library"
            print >> self.imports, "_libraries['MagickWand'] = CDLL(find_library('MagickWand'))"
            print >> self.imports, "_lib = _libraries['MagickWand']"
            self._c_libraries[dllname] = None
        return '_lib'

ctypeslib.codegen.codegenerator.Generator = IMGenerator # monkey-patch it

def _run_h2xml():
    p = subprocess.Popen(['MagickWand-config', '--cppflags'],
                         stdout=subprocess.PIPE)
    cpp_directives = p.stdout.read().decode().strip()
    include_dir = cpp_directives.split('-I')[1]
    argv = ['generate.py', cpp_directives, '-o', 'magickwand.xml',
            os.path.join(include_dir, 'wand/MagickWand.h')]
    return h2xml.main(argv)

def _run_xml2py():
    argv = ['generate.py', '-l', libname, '-r', '[A-Z]+.*', '-o', '_magickwand.py', 'magickwand.xml']
    return xml2py.main(argv)

if __name__ == "__main__":
    libname = ctypes.util.find_library('MagickWand')
    _run_h2xml()
    _run_xml2py()
