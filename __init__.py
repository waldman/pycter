#!/usr/bin/python


### Version Variable
_version = '0.1-Alpha'


### Inital Imports
from os import listdir
from os import path
from os import uname


### Error Classes
class Error(Exception):
    pass

class PlatformError(Error):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


### Defining platform and importing the correct functions
if uname()[0] == "Darwin":
    import Darwin 
    Platform = Darwin
elif uname()[0] == "Linux":
    import Linux
    Platform = Linux
else:
    raise PlatformError('The Platform ' + uname()[0] + ' is not Supported.')


### Main function
def Pycts():

    ### Modules:
    sys_modules_files = listdir(str(Platform.__name__))
    sys_modules = []

    ### Cleaning (Removing file ext and dups)
    for i in sys_modules_files:
        sys_modules.append(path.splitext(i)[0])

    sys_modules = list(set(sys_modules))

    sys_modules.remove('__init__')

    ### Building dictionary;
    pycts = {}
    for i in sys_modules:
        pycts.update(getattr(Platform, i).value(i))

    ### Adding Pycterversion
    pycts.update({'pycterversion': _version})

    return pycts


### If called from Terminal
if __name__ == "__main__":
    import sys
    pycts = Pycts()
    for key in sorted(pycts.iterkeys()):
        print "%s => %s" % (key, pycts[key])
    sys.exit(0)
