"""
=============
= uptime.py =
=============
"""
def value(name):
    """
    This function returns the following values:
    - uptime
    - uptime_days
    - uptime_hours
    - uptime_seconds
    """
    
    from os import popen

    uptime_raw = popen('uptime').read().split()
    if uptime_raw[3] == 'day' or uptime_raw[3] == 'days':
        uptime_total_days = uptime_raw[2]
        uptime_hours = uptime_raw[4].split(':')[0]
        uptime_minutes = uptime_raw[4].split(':')[1]
    else:
        uptime_total_days = '0'
        uptime_hours = uptime_raw[2].split(':')[0]
        uptime_minutes = uptime_raw[2].split(':')[1]

    uptime_total_hours = int(uptime_total_days) * 24 + int(uptime_hours)
    uptime_total_minutes = int(uptime_total_hours) * 60 + int(uptime_minutes.replace(',', ''))
    uptime_total_seconds = int(uptime_total_minutes) * 60

    value = dict({
        'uptime': ' '.join([uptime_total_days, 'days']),
        'uptime_days': uptime_total_days,
        'uptime_hours': uptime_total_hours,
        'uptime_seconds': uptime_total_seconds,
        })
    return value
