#!/usr/bin/python

import examples
import sys
import macfinder

if __name__ == '__main__':
    print 'Hello moto'

    print 'looking for macaddress in different formats'
    examples.find('9c:2a:70:7c:81:2d')
    examples.find('9c-2a-70-7c-81-2d')

    examples.sniffer = macfinder.Sniffer(sys.argv[1])
    examples.sniffer.startSniffing()
