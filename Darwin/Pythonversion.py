"""
====================
= pythonversion.py =
====================
"""
def value(name):
    """
    This function returns the following values:
    - pythonversion
    """
    import platform
    value = dict({
        'pythonversion': platform.python_version()
        })
    return value
