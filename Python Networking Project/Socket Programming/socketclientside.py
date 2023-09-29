'''Socket Programming
Socket programming is a way of connecting two software nodes (programs) on a network to have a two way communication
The server forms the listener socket on a port at the IP
The client reaches out to the server. 
"Mission control this is Violet wanting to speak with you"
" Hey I can hear you, ok no problem! Lets connect with each other, you ready?"
"Ready to go!"
# You know just did a three-way handshake to establlish a connection! 

'''

#Ok now set up a the client side to "speak" to github.com. Don't worry, if you do this right you will be talking soon!
import socket
import sys
# AddressFamily = IPV4 (Internet Procotcol Verison 4)
#SOCK_STREAM stands for Connection-Oriented TCP protocol- a mode to establish a connection before data is transferred
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket succesfully created: this is Violet, I would like to speak with you')
except socket.error as err:
    print(f'socket creation failed with error {err} oh no I will not be able to talk!')

port = 443

try:
    # a function to get the ip address of github.com by name (ping address in terminal to confirm the IP addresses match)
    host_ip = socket.gethostbyname('www.github.com')
    #exception if unable to resolve the host name (ip address) and connect to github.com. GAI stands for getaddrinfo()
except socket.gaierror:
    print('error resolving the host')
    sys.exit()
    # connect to the host and the port number you can do port 80 but port 443 is more secure!
client.connect((host_ip, port))
print(f'Socket has successfully connected to Github on port == {host_ip}, we can talk now!')