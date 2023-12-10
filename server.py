import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("192.168.60.79", 12345))
s.listen(10)
c,addr = s.accept()
print('{} connected.'.format(addr))
f = open('Dr_Stone.mp4', 'rb')

datas = f.read(1024)

while datas:
    c.send(datas)
    datas = f.read(1024)
f.close()
print("done sending")