#!/usr/bin/python

import sys
import os
import argparse
from macfinder import MAC
from macfinder import Database


def find(macaddress):
    macaddress = MAC.standarize_address(macaddress, 6)
    if MAC.validate(macaddress) is False:
        sys.exit("MAC error: Invalid ADDRESS")

    db = Database('csv',
            os.path.join(os.path.dirname(os.path.realpath(__file__)),
                "macaddress.io-db.csv"))

    res = db.find_mac_in_db(macaddress)
    for r in res:
        print "[+] FOUND: %s" % r


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='some desc')
#   TODO find better argument names
    parser.add_argument('-f', help='find vendor info by MAC address')

    args = parser.parse_args()

    if args.f is not None:
        find(args.f)
        sys.exit('[+] DONE')
    print args.f
