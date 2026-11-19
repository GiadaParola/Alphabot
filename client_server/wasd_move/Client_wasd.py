import socket
from pynput import keyboard

ip = "192.168.1.119"
porta = 13458

mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def on_press(key):
    try:
        if key.char == 'w':
            messaggio = "avanti"
        elif key.char == 'a':
            messaggio = "sinistra"
        elif key.char == 's':
            messaggio = "indietro"
        elif key.char == 'd':
            messaggio = "destra"
        else:
            return

        mySocket.sendto(messaggio.encode(), (ip, porta))
        print(messaggio)

    except AttributeError:
        pass

def on_release(key):
    messaggio = "stop"
    mySocket.sendto(messaggio.encode(), (ip, porta))
    print(messaggio)

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()