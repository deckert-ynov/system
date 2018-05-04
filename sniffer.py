#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket


def main():
    s = socket.socket(
            socket.AF_PACKET,
            socket.SOCK_RAW,
            socket.htons(3)
    )
    s.bind(('enp0s3', 3))

    while True:
        message = s.recv(1024)
        print(repr(message))


if __name__ == '__main__':
    main()
