import struct


class EthernetFrame(object):
    def __init__(self, payload):
        self.__parse_payload(payload)

    def __parse_payload(self, payload):
        self.__destination_address = struct.unpack('!BBBBBB', payload[0:6])
        self.__source_address = struct.unpack('!BBBBBB', payload[6:12])
        self.__ethertype = struct.unpack('!H', payload[12:14])

    @property
    def destination_address(self):
        return '{:0>2x}:{:0>2x}:{:0>2x}:{:0>2x}:{:0>2x}:{:0>2x}'.format(self.__destination_address[0],
                                                                        self.__destination_address[1],
                                                                        self.__destination_address[2],
                                                                        self.__destination_address[3],
                                                                        self.__destination_address[4],
                                                                        self.__destination_address[5])

    @property
    def source_address(self):
        return '{:0>2x}:{:0>2x}:{:0>2x}:{:0>2x}:{:0>2x}:{:0>2x}'.format(self.__source_address[0],
                                                                        self.__source_address[1],
                                                                        self.__source_address[2],
                                                                        self.__source_address[3],
                                                                        self.__source_address[4],
                                                                        self.__source_address[5])

    @property
    def ethertype(self):
        return '0x{:0>4x}'.format(self.__ethertype[0])
