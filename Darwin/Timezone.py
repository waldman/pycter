"""
Timezone.py
"""
def value(name):
    """
    This function returns the following values:
    - timezone
    """
    
    from os import popen

    timezone = popen('date +%Z').read()

    value = dict({
        'timezone': timezone,
        })
    return value
