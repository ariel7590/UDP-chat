import socket

UDP_IP = '0.0.0.0'
UDP_PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
sock.bind((UDP_IP, UDP_PORT))

clients = {}

while True:
    data, addr = sock.recvfrom(1024)
    if addr in clients.values():
        message = data.decode().split(' ')  # the message is made of 'name *space* message'
        content=''
        for i in range (1,len(message)):
            content=content+' '+message[i]
        me=''
        if message[0].encode() in clients:
            for key,value in clients.items():
                if value==addr:
                    me=key
            sendingContent = me.decode()+ ': ' + content
            sock.sendto(sendingContent.encode(), clients[message[0].encode()])
        else:
            sock.sendto("This client doesn't exist".encode(), addr)
    else:
        clients[data] = addr  # in this case, the data contains the users name
        sock.sendto(f'Hi {data.decode()}'.encode(), addr)
    print('received message:', data.decode())
