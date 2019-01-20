#!/usr/bin/python

import arpsniff

if __name__ == '__main__':
    print 'Hello moto'
    sniffer = arpsniff.Sniffer('eth0')
    sniffer.startSniffing()
