# MACfinder

At the bigining of this project I whished to have a tool to get vendor info from mac address.
After creating it, I thought it would be nice to have some kind of monitoring tool which works in background
and remebers all seenen network cards MAC address. In that way it would be easy to find not only vendor infos about mac address,
but also get info when and where we could saw before specified address.

## Usage
Please check `example.py` source for newest avaliable features, or you can run `runtest.sh` to check all features by one click.
```
./examples.py -f <macaddress>

$ ./examples.py b8:ca:3a:c5:ef:a4
[+] FOUND: {'oui': 'B8:CA:3A', 'countryCode': 'US', 'companyName': 'Dell Inc', 'companyAddress': 'One Dell Way Round Rock  TX  78682 US', 'dateCreated': '2013-01-09', 'assignmentBlockSize': 'MA-L', 'isPrivate': '0', 'dateUpdated': '2015-10-25'}
[+] DONE
```

Mac address should be atleast 24bits long. Accepted format: `XX:XX:XX`,`XX-XX-XX`, `XXXXXX`


Mac address database source [macaddress.io](https://macaddress.io/database-download/csv)
