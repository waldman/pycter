def value(name):
    """
    Return the Kernel name.
    """
    from os import uname
    value = dict({name: uname()[0]})
    return value
