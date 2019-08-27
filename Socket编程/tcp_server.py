# coding:utf-8

import socket
import datetime

HOST = '0.0.0.0'
# HOST = '127.0.0.1'
PORT = 3434

# AF_INET说明使用IPv4地址，SOCK_STREAM指明TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))  # 绑定IP与端口
s.listen(1)  # 监听

while True:
    conn, addr = s.accept()
    print('Client %s connected' % str(addr))
    dt = datetime.datetime.now()
    print(dt)
    message = 'Current time is ' + str(dt)
    # print(message)
    message = message.encode()  # encode编码，decode解码
    conn.send(message)  # send需要bytes类型对象
    print('Send: ', message)
    conn.close()