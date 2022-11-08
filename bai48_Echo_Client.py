import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = raw_input("Nhap dia chi IP cua Server: ")
try:
        s.connect((addr, 7777))
        while True:
                content1 = raw_input("Nhap chuoi: ")
                s.sendall(content1.encode())
                if (content1 == "#quit"):
                        break
                if (content1 == ''):
                        print "Hay nhap chuoi!"
                        continue
                content2 = s.recv(1024).decode()
                print "Ket qua:", content2
        s.close()

except EOFError:
        print "Loi nhap-xuat!"
except:
        print "Loi noi ket!"
