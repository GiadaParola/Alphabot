import socket

ip = "192.168.1.119"
porta = 13458

mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    messaggio = input("inserire un messaggio  ")

    mySocket.sendto(messaggio.encode(), (ip, porta))
    print("Messaggio mandato")

   # data, adr = mySocket.recvfrom(1024)

    