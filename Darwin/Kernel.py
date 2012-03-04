"""
=============
= kernel.py =
=============
"""
def value(name):
    """
    This function returns the following values:
    - hardwaremodel
    - kernel
    - kernelmajversion
    - kernelrelease
    - kernelversion
    - operatingsystem
    - operatingsystemrelease
    """
    from os import uname
    hardwaremodel = uname()[4]
    kernel = uname()[0]
    kernel_ver = uname()[2].split('.')
    kernelmajversion = '.'.join(kernel_ver[0:2])
    kernelrelease = uname()[2]
    kernelversion = uname()[2].split('-', 1)[0]
    value = dict({
        'hardwaremodel': hardwaremodel,
        'kernel': kernel,
        'kernelmajversion': kernelmajversion,
        'kernelrelease': kernelrelease,
        'kernelversion': kernelversion,
        'operatingsystem': kernel,
        'operatingsystemrelease': kernelrelease,
        })
    return value
