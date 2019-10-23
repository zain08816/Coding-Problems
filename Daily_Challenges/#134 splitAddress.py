import re
def splitAddress(address):
    address = re.split('\.|//|/|:', address)
    address.pop(1)
    address.pop(2)
    return address