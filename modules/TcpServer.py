import socket
import sys

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 65534))
server_socket.listen(5)

'''
The .accept() menthod blocks execution and waits for an incoming connection, it
returns a new socket object representing the connection and a tuple 
The tuple will contain (host,port) for IP4 connections or (host, port, flowinfo, scopedid)
for IPv6.
 imperative to understand is that you now have a new socket object from .accept().
 This is important because it's the socket that you'll use to communicate with the client.
 It's distinct from the listening socket that the server is using to accept new
 connections:
'''
while True:
    print("server waiting for connection!")
    c_socket,Addr=server_socket.accept()
    print("client connected from", Addr)

    while True:
        data=c_socket.recv(1024)
        if not data or data.decode('utf-8') =='END':
            break
        print("received from client client: %s" %data.decode("utf-8"))

        try:
            c_socket.send(('Hey client', 'utf-8'))
        except:
            print("Exited by the user")

    c_socket.close()
    server_socket.close()