from socket import *
import sys
import random

NUM_TRANSMISSIONS = 10



if len(sys.argv) > 4 or len(sys.argv) < 3:
    print("Usage: python3 " + sys.argv[0] + " server_address server_port [random_seed]")
    sys.exit(1)

if len(sys.argv) == 4:
    random_seed = int(sys.argv[3])
    random.seed(random_seed)

server_address = sys.argv[1]
server_port = int(sys.argv[2])



# TODO: Create a datagram socket for the client
sock_object=socket(AF_INET, SOCK_DGRAM)



# Repeat NUM_TRANSMISSIONS times
print()
for i in range(NUM_TRANSMISSIONS):

    rpc_data = ('prime(' + str(random.randint(0, 100)) + ')')
    print('sent: ' + rpc_data)

    sock_object.sendto(rpc_data.encode(), (server_address, server_port))

    serv_resp = sock_object.recvfrom(4096)



    if ((serv_resp[0].decode()) == 'True'):
        print('prime: yes\n')
    else:
        print('prime: no\n')

    

    

    # TODO: encode this data somehow (representing the integer as a string is fine) CHECK

    # TODO: Send RPC request (i.e., rpc_data) to the server 

    # TODO: Receive result back from the server into the variable result_data

    # TODO: Display it in the format "prime: yes" or "prime: no"

# TODO: Close any sockets that are open
sock_object.close()
