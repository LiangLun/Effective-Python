# coding:utf-8

import socket

HOST = '0.0.0.0'
PORT = 3434

# AF_INET说明使用IPv4地址，SOCK_DGRAM指明UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))  # 绑定IP与端口

# udp没有建立连接、断开连接的过程
while True:
    data, addr = s.recvfrom(1024)  # 本次接收最大数据长度是2014
    print('Received: %s from %s' % (data, str(addr)))

s.close()