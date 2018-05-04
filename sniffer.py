#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

from src.system.ethernet import EthernetFrame


def main():
    s = socket.socket(
            socket.AF_PACKET,
            socket.SOCK_RAW,
            socket.htons(3)
    )
    s.bind(('enp0s3', 3))

    counter = 0
    while True:
        counter += 1
        try:
            message = s.recv(1024)
            ethernet_frame = EthernetFrame(message)
            print('{:0>5d} - DSTADD: {}'.format(counter, ethernet_frame.destination_address))
            print('{:0>5d} - SRCADD: {}'.format(counter, ethernet_frame.source_address))
            print('{:0>5d} - ETHTYP: {}'.format(counter, ethernet_frame.ethertype))
        except KeyboardInterrupt:
            print('Sniffer stopped')
            break


if __name__ == '__main__':
    main()
