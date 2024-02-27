# TODO: import socket library
import sys
import random
import string
from socket import *


# Random alphanumeric string. Do not change
def rand_str(l):
    ret = ""
    for i in range(l):
        ret += random.choice(
            string.ascii_lowercase + string.ascii_uppercase + string.digits
        )
    return ret

if (len(sys.argv) > 3) or len(sys.argv) < 2:
    print("Usage: python3 " + sys.argv[0] + " server_port [random_seed]")
    sys.exit(1)

if len(sys.argv) == 3:
    random_seed = int(sys.argv[2])
    random.seed(random_seed)

server_port = int(sys.argv[1])

# TODO: Create a socket for the server on localhost
tcp_server = socket(AF_INET, SOCK_STREAM)

# TODO: Bind it to a specific server port supplied on the command line
tcp_server.bind(('0.0.0.0', server_port))

# TODO: Put server's socket in LISTEN mode
tcp_server.listen()

# TODO: Call accept to wait for a connection
(comm_socket, client_addr) = tcp_server.accept()



# TODO: receive data over the socket returned by the accept() method
data = ''
while(len(data) != 100):
    data += ((comm_socket.recv(4096)).decode())
#data2 = comm_socket.recv(4096)

# TODO: print out the received data for debugging
data_list = []
curr_str = ''
for i in range(len(data)):
    curr_str += data[i]
    if (i+1)%10 == 0:
        data_list.append(curr_str)
        curr_str = ''





# TODO: Generate a new string of length 10 using rand_str

for i in range(len(data_list)):
    print('\nreceived: ' + data_list[i])
    data_list[i] += rand_str(10)
    print('sending: ' + data_list[i])
    comm_socket.send(data_list[i].encode())


#print(data_list)

#comm_socket.send(data_list[i].encode())



    



# TODO: Append the string to the buffer received





# TODO: Send the new string back to the client


# TODO: Exit when client client closes connection
comm_socket.close()

# TODO: Close all sockets that were created
tcp_server.close()
