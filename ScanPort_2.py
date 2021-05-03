from socket import *
import time
startTime = time.time()

if __name__=='__main__':
        target = raw_input('Enter host to be scanned: ')
        t_IP = target
        print 'Starting scan on host: {}'.format(t_IP)
        try:
                for i in range(50,500):
                        s = socket(AF_INET, SOCK_STREAM)

                        conn = s.connect_ex((t_IP,i))
                        if conn == 0:
                                print 'Port {}: OPEN'.format(i)
                        s.close()
        except KeyboardInterrupt:
                print("\n Exitting Program !!!!")
                sys.exit()
        except socket.gaierror:
                print("\n Hostname Could Not Be Resolved !!!!")
                sys.exit()
        except socket.error:
                print("\ Server not responding !!!!")
                sys.exit()
print 'Time take:',(time.time() - startTime)