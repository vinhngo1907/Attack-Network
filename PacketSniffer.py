## Lap trinh phan tich va bat goi tin tren Python
import struct
import socket
import binascii
import os, sys
import time
def analyze_udp_header(data):
    udp_hdr = struct.unpack("!4H", data[:8])
    src_port = udp_hdr[0]
    dst_port = udp_hdr[1]
    length = udp_hdr[2]
    chk_sum = udp_hdr[3]
    data = data[8:]
    print "!___________________UDP HEADER______________________!"
    print "|\t\tSource:\t\t%hu" % src_port
    print "|\t\tDest:\t\t%hu" % dst_port
    print "|\t\tLength:\t\t%hu" % length
    print "|\t\tChecksum:\t%hu" % chk_sum
    return data

def analyze_tcp_header(data):
    tcp_hdr = struct.unpack("!2H2I4H", data[:20])
    src_port = tcp_hdr[0]
    dst_port = tcp_hdr[1]
    seq_num = tcp_hdr[2]
    ack_num = tcp_hdr[3]
    data_offset = tcp_hdr[4] >> 12
    reserved = (tcp_hdr[4] >> 6) & 0x03ff
    flags = tcp_hdr[4] & 0x003f
    urg = flags & 0x0020
    ack = flags & 0x0010
    psh = flags & 0x0008
    rst = flags & 0x0004
    syn = flags & 0x0002
    fin = flags & 0x0001
    window = tcp_hdr[5]
    checksum = tcp_hdr[6]
    urg_ptr = tcp_hdr[7]
    data = data[20:]
    print "!___________________TCP HEADER______________________!"
    print "|\t\tSource: \t%hu" % src_port
    print "|\t\tDest: \t\t%hu" % dst_port
    print "|\t\tSeq: \t\t%u" % seq_num
    print "|\t\tAck: \t\t%u" % ack_num
    print "|\t\tFlags:"
    print "|\t\t\t URG:%d" % urg
    print "|\t\t\t ACK:%d" % ack
    print "|\t\t\t PSH:%d" % psh
    print "|\t\t\t RST:%d" % rst
    print "|\t\t\t SYN:%d" % syn
    print "|\t\t\t FIN:%d" % fin
    print "|\t\t Window:\t%hu" % window 
    print "|\t\t Checksum:\t%hu" % checksum 
    return data

def analyze_ip_header(data):
    ip_hdr = struct.unpack("!6H4s4s", data[:20])
    ver = ip_hdr[0] >> 12
    ihl = (ip_hdr[0] >> 8) & 0x0f 
    tos = ip_hdr[0] & 0x00ff
    tot_len = ip_hdr[1]
    ip_id = ip_hdr[2]
    flags = ip_hdr[3] >> 13
    frag_offset = ip_hdr[3] & 0x1fff
    ip_ttl = ip_hdr[4] >> 8
    ip_proto = ip_hdr[4] & 0x00ff
    chk_sum = ip_hdr[5]
    src_addr = socket.inet_ntoa(ip_hdr[6]) #first 4s
    dst_addr = socket.inet_ntoa(ip_hdr[7]) #second 4s
    no_frag = flags >> 1
    more_frag = flags & 0x1 
    print "!___________________IP HEADER______________________!"
    print "|\t\tVersion:\t%hu" % ver
    print "|\t\tIHL:\t\t%hu" % ihl
    print "|\t\tTOS:\t\t%hu" % tos
    print "|\t\tLength:\t\t%hu" % tot_len
    print "|\t\tID:\t\t%hu" % ip_id
    print "|\t\tFlags:\t\t%hu" % flags
    print "|\t\tOffset:\t\t%hu" % frag_offset
    print "|\t\tTTL:\t\t%hu" % ip_ttl
    print "|\t\tNext Proto:\t%hu" % ip_proto
    print "|\t\tChecksum:\t%hu" % chk_sum
    print "|\t\tSource IP:\t%s" % src_addr
    print "|\t\tDest IP:\t%s" % dst_addr

    if ip_proto == 6:
        next_proto = "TCP"
    elif ip_proto == 17:
        next_proto = "UDP"
    else:
        next_proto = "Other"
    data = data[20:]
    return data, next_proto
def analyze_ether_header(data):
    ip_bool = False
    eth_hdr = struct.unpack("!6s6sH", data[:14]) #IPv4 = 0x0800
    dest_mac = binascii.hexlify(eth_hdr[0]) #Destination Address
    src_mac = binascii.hexlify(eth_hdr[1]) #Source Address
    proto = eth_hdr[2] >> 8 #NextProtocol
    print "!___________________ETH HEADER______________________!"
    print "|\tDestination MAC: \t%s:%s:%s:%s:%s:%s " % (dest_mac[0:2], dest_mac[2:4], dest_mac[4:6], dest_mac[6:8], dest_mac[8:10], dest_mac[10:12])
    print "|\tSource MAC: \t\t%s:%s:%s:%s:%s:%s" %(src_mac[0:2],src_mac[2:4],src_mac[4:6], src_mac[6:8], src_mac[8:10], src_mac[10:12])
    print "|\tProto:\t\t\t\t%hu" % proto
    if proto == 0x08:
        ip_bool = True
    data = data[14:]
    return data, ip_bool
def main():
    sniffer_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW,socket.ntohs(0x0003))
    recv_data = sniffer_socket.recv(2048)
    time.sleep(1)
    os.system("clear")
    data, ip_bool = analyze_ether_header(recv_data)
    if ip_bool:
        data, next_proto = analyze_ip_header(data)
    else:
        return
    if next_proto == "TCP":
        data = analyze_tcp_header(data)
    elif next_proto == "UDP":
        data = analyze_udp_header(data)
    else:
        return
while True:
    main()