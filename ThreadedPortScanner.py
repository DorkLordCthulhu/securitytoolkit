import socket
import threading
import time

class PortScanner:
    def __init__(self, min, max, server):
        self.range_min = int(min)
        self.range_max = int(max)
        self.server = server
        self.result_list = []
        self.thread_list = []

    def scan_port(self, port):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, self.range_max)
                s.settimeout(.1)
                s.connect((self.server, port))
                s.close()
                self.result_list.append(f"Port {port} is open")
            except TimeoutError:
                pass
            except socket.timeout:
                pass

    def threader(self):
        start_time = time.time()
        for port in range(self.range_min, self.range_max):
            thr = threading.Thread(target= self.scan_port, args=(port,))
            thr.start()
            self.thread_list.append(thr)
            if len(self.thread_list) >= 30:
                for thread in self.thread_list:
                    thread.join()
                self.thread_list = [x for x in self.thread_list if x.isAlive()]
        for thread in self.thread_list:
            thread.join()
        return self.result_list, f"took{time.time()-start_time} seconds"


if __name__ == '__main__':
    print_lock = threading.Lock()
    server = input("PUT TARGET SERVER/SITE HERE")
    min = int(input("What port number shall we start at?"))
    max = int(input("At what port number shall we stop?"))
    y = PortScanner(min, max, server)
    print (y.threader())
