import socket
import struct

class PacketSniffer:
    def __init__(self):
        self.data = ""
        self.destination = ""
        self.source = ""
        self.protocol = ""

    def eth_frame(self):
        self.destination, self.source, self.protocol = struct.unpack('! 6s 6s H', self.data[:14])

    def get_mac(self, bytesaddr):
        bytes_str = map('{:02x}'.format, bytesaddr)
        mac_addr = ':'.join(bytes_str).upper()
        return mac_addr

    def get_eth_info(self):
        return PacketSniffer.get_mac(self.destination),PacketSniffer.get_mac(self.source),PacketSniffer.get_mac(self.protocol)

    def sniffer(self):
        connection = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
        while True:
            raw_data, addr = connection.recvfrom(65535)
            destination_mac, source_mac, protocol, data= PacketSniffer.get_mac(raw_data)
            return (f"Destination: {destination_mac} Source: {source_mac} Protocol: {protocol}")

if __name__ == '__main__':
    x = PacketSniffer
    x.eth_frame()
    x.sniffer()
