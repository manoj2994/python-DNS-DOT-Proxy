import socket,socketserver,threading
import ssl,sys

NAMESERVER='1.1.1.1'
HOST='172.17.0.2'
PORT=53
BUFFER_SIZE=1024

def tls_bind(data,hostname):
    context = ssl.create_default_context()

    with socket.create_connection((hostname, 853)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            ssock.send(data)
            return ssock.recv(1024)

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            self.data = tls_bind(self.request.recv(1024),hostname=NAMESERVER)
            print("connected {}".format(self.client_address[0]))
            self.request.send(self.data)
        except socket.error as err:
            print("Error: ",err)
            self.request.close()
            sys.exit(1)
            
            
class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
           data = self.request[0]
           socket = self.request[1]
           res = self.to_tcp(data) 
           udp_query = tls_bind(res,NAMESERVER)
           print("connected {}".format(self.client_address[0]))
           socket.sendto(udp_query,self.client_address)
        except socket.error as err:
            print("Error: ",err)
            self.request.close()
            sys.exit(1)
            
    def to_tcp(msg):
        packet_len = bytes([00])+bytes([len(msg)])
        packet = packet_len + packet
        return packet

if __name__ == "__main__":
    tcpserver = socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
    tcp_process = threading.Thread(target=tcpserver.serve_forever)
    tcp_process.start()
    udpserver = socketserver.ThreadingUDPServer((HOST,PORT),MyUDPHandler)
    udp_process = threading.Thread(target=udpserver.serve_forever)
    udp_process.start()   