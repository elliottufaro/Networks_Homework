import sys
import random
import string
from socket import *

RAND_STR_LEN = 10


# TODO: Import socket library


# Random alphanumeric string. Do not change
def rand_str():
    ret = ""
    for i in range(RAND_STR_LEN):
        ret += random.choice(
            string.ascii_lowercase + string.ascii_uppercase + string.digits
        )
    return ret


NUM_TRANSMISSIONS = 10


def client_socket_setup(server_port, server_address):
    pass
    # TODO: Create and return the socket for the client
    tcp_client = socket(AF_INET, SOCK_STREAM)

    # TODO:  Connect this socket to the server
    tcp_client.connect((server_address, server_port))

    return tcp_client



def transmit_using_socket(client_socket):
    # Transmit NUM_TRANSMISSIONS number of times
    pre_concatenate = []
    post_concatenate = []
    for i in range(NUM_TRANSMISSIONS):
        pass
        # TODO: Generate a random string of length 10 using rand_str function
        randString = (rand_str())

        pre_concatenate.append(randString)

        #print(randString)

        # TODO: Send random string to the server
        client_socket.send(randString.encode())

        # TODO: Print data for debugging
        #print(randString)

        # TODO: Receive concatenated data back from server as a byte array

    #x = (client_socket.recv(4096)).decode()
    concatenated_data = ''
    while(len(concatenated_data) != 200):
        #print(concatenated_data)
        concatenated_data += ((client_socket.recv(4096)).decode())

    #print(concatenated_data)

    curr_str = ''
    for i in range(len(concatenated_data)):
        curr_str += concatenated_data[i]
        if (i+1)%20 == 0:
            post_concatenate.append(curr_str)
            curr_str = ''

    for i in range(len(pre_concatenate)):
        print('\nsent: ' + pre_concatenate[i])
        print('received: ' + post_concatenate[i])
    

        # TODO: Print out concatenated data for debugging

        # TODO: Close socket
    client_socket.close()

    


if __name__ == "__main__":
    if len(sys.argv) > 4 or len(sys.argv) < 3:
        print("Usage: python3 " + sys.argv[0] + " server_address server_port [random_seed]")
        sys.exit(1)

    if len(sys.argv) == 4:
        random_seed = int(sys.argv[3])
        random.seed(random_seed)

    server_address = sys.argv[1]
    server_port = int(sys.argv[2])

    client_socket = client_socket_setup(server_port, server_address)
    transmit_using_socket(client_socket)
