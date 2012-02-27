"""
=============
= Domain.py =
=============
"""
def value(name):
    """
    This function returns the following values:
    - domain
    - hostname
    - fqdn
    """
    from socket import getfqdn

    fqdn = getfqdn()
    split_fqdn = fqdn.split('.', 1)
    hostname = split_fqdn[0]
    domain = split_fqdn[1]

    value = dict({
        'domain': domain,
        'fqdn': fqdn,
        'hostname': hostname,
        })
    return value
