
import socket
import time
import sys
 
HOST_IP = "192.168.12.1"    #我的树莓派作为AP热点的ip地址
HOST_PORT = 7654            #端口号
 
print("Starting socket: TCP...")
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #创建socket
 
print("TCP server listen @ %s:%d!" %(HOST_IP, HOST_PORT) )
host_addr = (HOST_IP, HOST_PORT)
socket_tcp.bind(host_addr)    #绑定我的树莓派的ip地址和端口号
socket_tcp.listen(1)	#listen函数的参数是监听客户端的个数，这里只监听一个，即只允许与一个客户端创建连接
 
while True:
	print ('waiting for connection...')
	socket_con, (client_ip, client_port) = socket_tcp.accept()    #接收客户端的请求
	print("Connection accepted from %s." %client_ip)
 
	socket_con.send("Welcome to RPi TCP server!")    #发送数据
 
	while True:
		data=socket_con.recv(1024)    #接收数据
		
		if data:    #如果数据不为空，则打印数据，并将数据转发给客户端
			print(data)
			socket_con.send(data)
 
socket_tcp.close()