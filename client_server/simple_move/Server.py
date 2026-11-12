
from AlphaBot import AlphaBot
import socket
import time

alpha = AlphaBot()
ip = "192.168.1.101"
porta = 13458

alpha.stop()

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(("0.0.0.0", 13458))
print(f"Connessione riuscita al PC")


try: 

    while True:
    
        data, addr = serverSocket.recvfrom(1024)
        comando = data.decode()
        print(f"Ricevuto da {addr}: {comando}")

        match comando:

            case "avanti":
                alpha.forward()

            case "indietro":
                alpha.backward()
                
            case "destra":
                alpha.right()
                
            case "sinistra":
                alpha.left()

            case _:
                alpha.stop()

        
        time.sleep(1)
        alpha.stop()
                

    alpha.stop()


except KeyboardInterrupt:
    alpha.stop()