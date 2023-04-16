import socket

HOST = ''  # this represents the server's hostname or IP address
PORT = 12345  # a port number that the server will listen on

# create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # bind the socket to a specific address and port
    s.bind((HOST, PORT))

    # listen for incoming connections (backlog argument specifies the maximum number of queued connections)
    s.listen(1)
    print(f"Server listening on port {PORT}...")

    # accept incoming connection requests
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")

        # receive data from the client
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received data: {data.decode()}")

            # send a response back to the client
            conn.sendall(b"Message received!")

