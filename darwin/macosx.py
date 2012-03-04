"""
=============
= macosx.py =
=============
"""
def value(name):
    """
    This function returns the following values:
    - all macosx prefixed pycts
    - all sp prefixed pycts
    """

    ### Importing
    from os import popen
    from plistlib import readPlistFromString

    ### Fetching the Data from OS
    sys_profile = popen('/usr/sbin/system_profiler -xml 2> /dev/null').read()
    sys_profile_dict = readPlistFromString(sys_profile)

    ### Filtering the interesting bits from the output
    for i in sys_profile_dict:
        if i['_dataType'] == "SPHardwareDataType":
            sph = i['_items']
        elif i['_dataType'] == "SPSoftwareDataType":
            sps = i['_items']

    ### Removing _name key
    del sph[0]['_name']
    del sps[0]['_name']

    ### Creating raw unified dict
    raw_value = {}
    raw_value.update(sph[0])
    raw_value.update(sps[0])

    value = {}

    ### Creating macosx prefixed values
    macosx = raw_value['os_version']
    macosx_split = macosx.split()
 
    value.update({
        'macosx_buildversion': macosx_split[4][1:7],
        'macosx_productname': ' '.join([macosx_split[0], macosx_split[1], macosx_split[2]]),
        'macosx_productversion': macosx_split[3],
        'macosx_productversion_major': '.'.join([macosx_split[3].split('.')[0], macosx_split[3].split('.')[1]]),
        'macosx_productversion_minor': macosx_split[3].split('.')[2],
        })

    ### Adding sp prefixed values to main dict
    for key, data in raw_value.items():
        key = '_'.join(['sp', key])
        value.update({key.lower(): data})

    return value
