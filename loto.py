import random
pool = [n for n in range(1,42)]
elegido = random.choice(pool)
print("El primer número es", elegido)
# sacamos el 2do, pero debemos evitar que se vuelva
# a sacar el número anterior
pool.remove(elegido)
elegido = random.choice(pool)
print("El segundo número es", elegido)