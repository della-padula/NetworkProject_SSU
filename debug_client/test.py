from socket import *

ip = 'localhost'
port = 9090

while(True):
	s = socket(AF_INET, SOCK_STREAM)
	s.connect((ip,port))
	s.send("\x00\x00\x00\x00\x00\x00\x00\x00\x41\x41\x41\x41")
	print s.recv(1024)
	s.send("\x00\x00\x00\x01\x13\x37\x13\x37\x42\x42\x42\x42\x42\x42\x42")
	print s.recv(1024)
	s.send("\x00\x00\x00\x02\x41\x41\x41\x41\x41")
	print s.recv(1024)
	s.close()
