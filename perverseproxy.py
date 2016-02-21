import sys
import socket
import urllib2


HOST, PORT = sys.argv[1].split(":")
PORT = int(PORT)

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

print HOST + ":" + str(PORT)

while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)

    request = request.splitlines()
    url = "http://" + request[1][6:] + request[0][4:-8]
    print url
    response = urllib2.urlopen(url)
    malmsg = "badboy"
    malcode = response.read()
    malcode += malmsg
    http_response = malcode

    client_connection.sendall(http_response)
    client_connection.close()
