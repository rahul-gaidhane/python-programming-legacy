import socket

host = "127.0.0.1"
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
message = "this is my message"
print("inside client")
while True:
    s.send(message.encode('ascii'))
    print("this client")
    data = s.recv(1024)

    print("Received from server :", str(data.decode('ascii')))

    ans = input('\nDo you want to continue(y/n) :')
    if ans == 'y':
        continue
    else:
        break
s.close()
