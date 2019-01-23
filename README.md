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
```
$ ./runtest.sh wlan0
[sudo] password:
Hello moto
looking for macaddress in different formats
9C2A70
[+] FOUND: {'oui': '9C:2A:70', 'countryCode': 'CN', 'companyName': 'Hon Hai Precision Ind. Co, Ltd', 'companyAddress': 'Building D21,No.1, East Zone 1st Road Chongqing  Chongqing  401332 CN', 'dateCreated': '2013-01-09', 'assignmentBlockSize': 'MA-L', 'isPrivate': '0', 'dateUpdated': '2016-05-31'}                                         
9C2A70
[+] FOUND: {'oui': '9C:2A:70', 'countryCode': 'CN', 'companyName': 'Hon Hai Precision Ind. Co, Ltd', 'companyAddress': 'Building D21,No.1, East Zone 1st Road Chongqing  Chongqing  401332 CN', 'dateCreated': '2013-01-09', 'assignmentBlockSize': 'MA-L', 'isPrivate': '0', 'dateUpdated': '2016-05-31'}                                         
mhmmm...
src: 30b5c24bb7d4 dest: 000000000000
src: 9c2a707c812d dest: 30b5c24bb7d4
src: 30b5c24bb7d4 dest: 000000000000
src: 9c2a707c812d dest: 30b5c24bb7d4
```

Mac address should be atleast 24bits long. Accepted format: `XX:XX:XX`,`XX-XX-XX`, `XXXXXX`


Mac address database source [macaddress.io](https://macaddress.io/database-download/csv)
