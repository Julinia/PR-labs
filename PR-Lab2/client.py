import socket
import ssl
from dtls import do_patch

from pprint import pprint

TARGET_HOST ='localhost'
TARGET_PORT = 8000
CA_CERT_PATH = 'server.crt'
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT = 12345
buffer=4096

do_patch()
address = (UDP_IP_ADDRESS ,UDP_PORT)
socket_client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    ssl_conn = ssl.wrap_socket(socket_client, cert_reqs=ssl.CERT_REQUIRED, ssl_version=ssl.PROTOCOL_TLSv1, ca_certs=CA_CERT_PATH)
    target_host = TARGET_HOST 
    target_port = TARGET_PORT 
    ssl_conn.connect((target_host, int(target_port)))
    # get remote cert
    cert = ssl_conn.getpeercert()
    print("Checking server certificate")
    pprint(cert)
    if not cert or ssl.match_hostname(cert, target_host):
        raise Exception("Invalid SSL cert for host %s. Check if this is an attack!" %target_host )
    print("Server certificate OK.\n Sending some custom request... GET ")
    ssl_conn.write('GET / \n'.encode('utf-8'))
    print("Response received from server:")
    print(ssl_conn.read())
    ssl_conn.close()
    message = input('Enter your message: ')
    if message=="exit":
        break
    socket_client.sendto(message.encode(),address)
    response,addr = socket_client.recvfrom(buffer)
    print("Server response => %s" % response)

socket_client.close()