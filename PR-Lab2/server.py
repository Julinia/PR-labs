import socket,sys
import ssl

SSL_SERVER_PORT = 8000
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT = 12345
buffer=4096

socket_server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
socket_server.bind((UDP_IP_ADDRESS,UDP_PORT))

while True:
    print("Waiting for client...")
    print("Waiting for ssl client on port %s" %SSL_SERVER_PORT)
    data1, addr = socket_server.recvfrom(buffer)
    print(data1, addr)
    ssl_conn = ssl.wrap_socket(data1, server_side=True, certfile="server.crt", keyfile="server.key", ssl_version=ssl.PROTOCOL_TLSv1)
    print(ssl_conn.read())
    ssl_conn.write('200 OK\r\n\r\n'.encode())
    print("Served ssl client. Exiting...")
    ssl_conn.close()
    data,address = socket_server.recvfrom(buffer)
    data = data.strip()
    print("Data Received from address: ",address)
    print("message: ", data)
    try:
        response = "Hello %s" % sys.platform
    except Exception as e:
        response = "%s" % sys.exc_info()[0]
    
    print("Response",response)
    socket_server.sendto(response.encode(),address)
    
socket_server.close()