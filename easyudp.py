import socket
from time import sleep
def tx(ip,port,msg): # Transmit a message - IP, Port, message
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.sendto(msg, (ip, port))
def rx(my_ip,my_port,ack=True): # Receive a message, return it's content and end function - IP of device, Port to listen at
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind((my_ip, my_port))
        data, addr = sock.recvfrom(1024)
	if ack != False:
		coords = str(addr).split("'")
		ackip = coords[1]
		tx(ackip,my_port,"ACK")
	return data
def rx_ack(my_ip,my_port): # After transmitting a message, wait for ACK
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((my_ip, my_port))
        sock.settimeout(10)
        try:
                data, addr = sock.recvfrom(1024)
        except socket.timeout:
                return False
        if data:
                if data == "ACK":
                        return True
                else:
                        return False
        else:
                return False
