import sys
import ctypes.util
import ctypeslib.codegen.codegenerator

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

if __name__ == "__main__":
    from ctypeslib.xml2py import main
    libname = ctypes.util.find_library('MagickWand')
    argv = ['generate.py', '-l', libname, '-r', '[A-Z]+.*', '-o', 'wand.py', 'wand.xml']
    sys.exit(main(argv))
