'''
class represents MAC address
'''
import re


class MAC:

    def __init__(self):
        pass

    @staticmethod
    def standarize_address(mac, length=-1):
        bad_chars = [':', '-']
        for char in bad_chars:
#           debug
#           print bad_chars
            mac = mac.replace(char, '')

        if length != -1:
            mac = mac[:length]

        return mac.strip().upper()

    @staticmethod
    def validate(address):
        print address
        if len(address) >= 6 and re.match('[A-F0-9]', address) is not None:
            return True

        return False
