import time
from AlphaBot import AlphaBot  # Importa la classe dal file AlphaBot.py

# Inizializza l'istanza di AlphaBot
# (Nota: appena viene creato l'oggetto, il robot parte automaticamente in avanti per via del codice __init__)
robot = AlphaBot()

try:
    robot.square()

    robot.stop()

except KeyboardInterrupt:
    # Interrompe il robot in sicurezza se premi Ctrl+C
    robot.stop()
    print("\Programma terminato dall'utente.")