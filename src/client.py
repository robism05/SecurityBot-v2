import socket

HOST = '2.122.85.82'  # replace this with the IP address or hostname of the server
PORT = 12345  # the port number that the server is listening on

# create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # connect to the server
    s.connect((HOST, PORT))

    # send data to the server
    message = "Hello, server!"
    s.sendall(message.encode())

    # receive a response from the server
    data = s.recv(1024)
    print(f"Received response: {data.decode()}")

