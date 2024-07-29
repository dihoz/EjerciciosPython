import time
import sys

def mecanografiar(texto):

 lista = texto.split()

 for palabra in lista:
    sys.stdout.write(palabra + " ")
    sys.stdout.flush()
    time.sleep(4)

print("\n")
mecanografiar("Hola mundo Python Rules!")
print("\n")