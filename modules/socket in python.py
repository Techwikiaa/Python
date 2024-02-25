import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket created")
    print("Connecting...")
except socket.error as err:
    print("socket failed to create due to %s" %(err))

target_host = input("Enter a website address: ")
target_port = 443


try:
    s.connect((target_host, target_port))
    print("Sucessfully connect to %s with %d port." %(target_host, target_port))
    s.shutdown(2)
except socket.error as err:
    print("unable to build socket connection %s with %d port" %(target_host, target_port))
    print("unable to build socket %s" %(err))
    sys.exit()

    

