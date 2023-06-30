import sys, socket
from os import listdir
from os.path import isfile, join
from ServerWorker import ServerWorker

class Server:
    def main(self):
        try:
            SERVER_PORT = int(sys.argv[1])
        except:
            print("[Usage: Server.py Server_port]\n")
        rtspSocket = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)

        rtspSocket.bind(('', SERVER_PORT))
        rtspSocket.listen(5)
        fileSocket = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)
        fileSocket.bind(('',12345))
        fileSocket.listen(1)
        n = 0
        # Receive client info (address, port) through RTSP/TCP session

        while true:
            clientInfo = {}
            clientInfo['rtspSocket'] = rtspSocket.accept()
            clientInfo['fileSocket'] = fileSocket.accept()
            ServerWorker(clientInfo).run()

if __name__ == "__main__":
    (Server()).main()