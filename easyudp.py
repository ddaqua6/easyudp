import socket
def tx(ip,port,msg): # Transmit a message - IP, Port, message
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.sendto(msg, (ip, port))
def rx(my_ip,my_port): # Receive a message, return it's content and end function - IP of device, Port to listen at
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind((my_ip, my_port))
        data, addr = sock.recvfrom(1024)
        return data
def rx_while_true(my_ip,my_port): # Receive a message, return it's content and keep function running
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind((ip, port))
	while True:
        	data, addr = sock.recvfrom(1024)
        	return data
