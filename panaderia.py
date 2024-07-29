"""
Una panadería vende (H)allullas, (M)arraquetas, pan (P)ita e (I)ntegral
El kilo de cada uno es 1990, 2010 y 2500 respectivamente
El programa debe solicitar al usuario la cantidad en gramos de pan que quiere llevar
y su tipo.
Hoy la panaderia tiene una promomción, por cada 3 Kilos de pan, se regala un alfajor.
(Excepto por compra de pan integral)

Cuando el programa finalice se debe indicar los datos de entrada, salida e indicar 
si el cliente obtuvo o no de regalo uno o más alfajores
"""
class panaderia():
    import os
    import math
    i="a"
    while i!="q":
        os.system("cls")
        print("\n   -----            PANADERÍA           -----\n")
        print("   ------------------------------------------------------\n")
        #Precios
        ph=1990 #Hallula
        pm=2010 #marraqueta
        pp=2500 #pita
        pi=2600 #integral
        a=0 #alfajor
        pan=str(input("\n(H)allullas\n(M)arraquetas\npan (P)ita\n(I)ntegral\nIngrese el tipo de pan: "))
        peso=float(input("Ingrese el peso del pan en gramos : "))
        #precio=float(input("Ingrese el precio unitario : "))
        a=peso//3000
        peso=peso/1000
        if pan=="H" or pan=="h":
            pan="Hallulla"
            precio=peso*ph
        elif pan=="M" or pan=="m":
            pan="Marraqueta"
            precio=peso*pm
        elif pan=="P" or pan=="p":
            pan="Pan Pita"
            precio=peso*pp
        elif pan=="I" or pan=="i":
            pan="Integral"
            precio=peso*pi
            a=0
        else:
            pan="Otro tipo de Pan"
            precio=peso*pi
            a=0
                
        print(f"\nEl pan seleccionado es {pan}\ncon cantidad en kilos es {peso} \nel precio total es {precio}\n -------------------------------------")
        if pan!="Integral":
            print(f"Por su compra le reglamos {a} alfajores\n -------------------------------------")
        i=str(input("ingrese \"q\" para salir \"c\" para continuar : "))

panaderia()