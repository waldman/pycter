#!/usr/bin/python


### Inital Imports
from os import listdir, path, uname


### Version Variable
_version = '0.1-Alpha'


### Error Classes
class Error(Exception):
    pass


class PlatformError(Error):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


### Defining platform and importing the correct function set
if uname()[0] == "Darwin":
    import darwin 
    platform = darwin
elif uname()[0] == "Linux":
    import linux
    platform = linux
else:
    raise PlatformError('The platform ' + uname()[0] + ' is not Supported.')


### Functions
def pycts(key = ''):
    sys_modules = platform.funcList()

    pycts = {}
    for i in sys_modules:
        pycts.update(getattr(platform, i).value(i))

    ### Adding Pycterversion
    pycts.update({'pycterversion': _version})

    if key:
        try:
            return pycts[key]
        except:
            print ''.join(['The key "', key, '" is not mapped or missing'])

    else:
        return pycts


### If called from Terminal
if __name__ == "__main__":
    import sys
    pycts_dict = pycts()
    for key in sorted(pycts_dict.iterkeys()):
        print "%s => %s" % (key, pycts_dict[key])
 
    pycts() 
 
    sys.exit(0)
