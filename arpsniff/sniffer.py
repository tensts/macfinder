'''
Simple class to listen,parse and filter ARP requests
'''
import socket
import struct
import binascii

class Sniffer:
    
    socket = -1
    interface_name = ''
    run = False
    
    def __init__(self, eth_name):
        self.socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))
        self.interface_name = eth_name

        self.socket.bind((self.interface_name,0))


    def startSniffing(self):
        self.run = True
        self.sniff()

    def sniff(self):
        print 'mhmmm...'
        while self.run:
            packet = self.socket.recv(42)
            #print packet[0:32].encode('hex')
            if struct.unpack('!6s6s2s', packet[:14])[2] == '\x08\x06':
                arp = struct.unpack('2s2s1s1s2s6s4s6s4s',packet[14:42])
                print 'src: %s dest: %s' % (binascii.hexlify(arp[5]), binascii.hexlify(arp[7]))

