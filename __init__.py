#!/usr/bin/python

_version = '0.1'

from os import listdir
from os import path
from os import uname

def Pycts():
    Plataform = __import__(uname()[0])
    
    # Modules:
    sys_modules_files = listdir(str(Plataform.__name__))
    sys_modules = []

    # Cleaning (Removing file ext and dups)
    for i in sys_modules_files:
        sys_modules.append(path.splitext(i)[0])

    sys_modules = list(set(sys_modules))

    sys_modules.remove('__init__')

    # Building dictionary;
    pycts = {}
    for i in sys_modules:
        pycts.update(getattr(Plataform, i).value(i))

    # Adding Pycterversion
    pycts.update({'Pycterversion': _version})

    return pycts


if __name__ == "__main__":
    import sys
    pycts = Pycts()
    for key in sorted(pycts.iterkeys()):
        print "%s => %s" % (key, pycts[key])
    sys.exit(0)
