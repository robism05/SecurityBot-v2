import socket,platform

h_name = socket.gethostname()
IP_address = socket.gethostbyname(h_name)
print("Operating System: "+platform.system())
print("Host Name is: " + h_name)
print("Computer IP Address (localhost) is: " + IP_address)


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
        if IP.startswith('172'):
            print("USER ROUTER NOT COMPATIBLE")
    except Exception:
        IP = '127.0.0.1'     
    finally:
        s.close()
    return IP



print(get_ip())
