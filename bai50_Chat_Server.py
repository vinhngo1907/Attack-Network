import socket
import select
def chat(i, message):
    for j in clients:
        if j != s and j != i:
            try:
                j.sendall(message.encode())
            except:
                j.close()
                clients.remove(j)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 8888))
s.listen(6)
clients = []
clients.append(s)
print "Da khoi tao xong Chat Server."

while True:
    try:
        input, output, err = select.select(clients, [], [])
        for i in input:
            if (i == s):
                cli, (addr, port) = s.accept()
                clients.append(cli)
                print "Client", addr, "connected."
                chat(i, "%s da vao phong chat.\n" %addr)
            else:
                try:
                    data = i.recv(1024).decode()
                    if (data == "#quit"):
                        i.close()
                        clients.remove(i)
                        print "Client dia chi", addr, "dong noi ket!"
                        chat(i, "%s da roi phong chat!\n" %addr)
                    else:
                        chat(i, '<' + addr + '> ' + data + "\n")
                except:
                    i.close()
                    clients.remove(i)
                    print "Client dia chi", addr, "ngat noi ket!"
                    chat(i, "%s da thoat khoi phong chat!\n" %addr)
                    continue
    except KeyboardInterrupt:
        print "Chuong trinh co the bi gian doan."
