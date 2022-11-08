import socket
host_name = socket.gethostname()
print "Ten cua may tinh cuc bo (Host name): %s" %host_name

addr = socket.gethostbyname_ex("www.google.com")[-1]
print "Dia chi IP cua www.google.com:"
for ip in addr:
    print ip

ipAddr = "172.18.63.194"
host_name_2 = socket.gethostbyaddr(ipAddr)[0]
print "Ten may tinh co dia chi 172.18.63.194 la: %s" %host_name_2
