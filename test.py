import socket


# http
def http():
    a = socket.socket()
    a.bind(("0.0.0.0", 0))
    a.connect(("192.168.1.1", 80))
    a.send(b"GET / HTTP/1.0\r\nHost: 192.168.1.1\r\n\r\n")
    _ = a.recv(1024)
    data = b""
    while z:
        data = data + _
        _ = a.recv(1024)
    print(data)


http()
