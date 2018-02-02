#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定端口
s.bind(('127.0.0.1',9999))
print('bind udp on 9999')
while True:
    #接受数据
    data,addr=s.recvfrom(1024)
    print('received from %s:%s.' % addr)
    reply='hello,%s!'%data.decode('utf-8')
    s.sendto(reply.encode('utf-8'),addr)
