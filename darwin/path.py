"""
===========
= path.py =
===========
"""
def value(name):
    """
    This function returns the following values:
    - path
    """

    from os import environ

    path = environ['PATH']

    value = dict({
        'path': path,
        })
    return value
