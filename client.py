import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("192.168.197.179", 65000))

f = open('ss.mp4', 'wb')


while True:
    datas = s.recv(1024)
    while datas:
        f.write(datas)
        datas = s.recv(1024)
    f.close()
    break
print("done receiving")