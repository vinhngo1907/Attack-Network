import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)
try:
    s.connect(('127.0.0.1', 8888))
    print "Da noi ket den Chat Server. Tro chuyen ngay bay gio!"
    print "Nhan enter de cap nhat doan chat moi."
    message_1 = s.recv(1024).decode()
    print message_1
    while True:
        try:
            message_2 = s.recv(1024).decode()
            sys.stdout.write(message_2)
            sys.stdout.flush()
            continue
        except socket.timeout:
            message_3 = raw_input("Ban: ")
            if (message_3 == ""):
                continue
            else:
                s.sendall(message_3.encode())
                if (message_3 == "#quit"):
                    break
                continue
    s.close()
except IOError:
    print "Loi nhap-xuat!"
except:
    print "Loi noi ket!"
    
