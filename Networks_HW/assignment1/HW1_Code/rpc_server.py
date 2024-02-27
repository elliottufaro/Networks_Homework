import sys
from socket import *
import signal

NUM_TRANSMISSIONS = 10
if len(sys.argv) < 2:
    print("Usage: python3 " + sys.argv[0] + " server_port")
    sys.exit(1)
assert len(sys.argv) == 2
server_port = int(sys.argv[1])

# TODO: Create a socket for the server
sock_receiver = socket(AF_INET, SOCK_DGRAM)

# Setup signal handler to exit gracefully
def cleanup(sig, frame):
    # TODO Close server's socket
    sock_receiver.close()
    sys.exit(0)

def prime(n):
    print()
    print(n)
    if n <= 1:
        return False 
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

    

# SIGINT is sent when you press ctrl + C, SIGTERM if you use 'kill' or leave the shell
signal.signal(signal.SIGINT, cleanup)
signal.signal(signal.SIGTERM, cleanup)


# TODO: Bind it to server_port
sock_receiver.bind(('0.0.0.0', server_port))
#x = sock_receiver.recv(4096)
#print(x)



while True:
    pass
    # TODO: Receive RPC request from client
    rpc_data = (sock_receiver.recvfrom(4096))
    #print(rpc_data[0])
    val = list(rpc_data[0].decode())
    address = rpc_data[1]
    
    val.pop()
    for i in range(6):
        val.pop(0)
    #print(address)
    ret_val = (str(prime(int(''.join(val))))).encode()


    sock_receiver.sendto(ret_val, (address[0], address[1]))
    #print(prime(int(''.join(val))))
        

    # TODO: Turn byte array that you received from client into a string variable called rpc_data

    # TODO: Parse rpc_data to get the argument to the RPC.
    # Remember that the RPC request string is of the form prime(NUMBER)

    # TODO: Print out the argument for debugging

    # TODO: Compute if the number is prime (return a 'yes' or a 'no' string)

    # TODO: Send the result of primality check back to the client who sent the RPC request

# TODO: Close server's socket
sock_receiver.close()
