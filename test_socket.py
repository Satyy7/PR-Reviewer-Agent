import socket

try:
    s = socket.socket()
    s.settimeout(5)

    s.connect(("localhost", 6379))

    print("CONNECTED")

    print(s.recv(1024))

except Exception as e:
    print(type(e))
    print(e)