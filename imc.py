'''
Desarrollar un programa que permita obtener el IMC de una
persona a partir de su peso en kilogramos y su estatura en metros.
IMC =     peso
       ----------
        estatura^2
'''
class imc():
        import math
        i="a"
        while i!="q":
                print("\n   -----          IMC         -----\n")
                print("   ----- Cálculo de IMC, segun su peso y su altura   -----\n")
                #print(" Datos: \n Margen 20% \n IVA 19% \n")
                peso=float(input("Ingrese peso (sin mentir por favor) : "))
                altura=float(input("Ingrese su altura : "))
                resultado = peso / math.pow(altura,2)
                print(f"-------------------------------------\nsu IMC es :{resultado:.3f}Kg/m'2 \n-------------------------------------")
                i=str(input("ingrese \"q\" para salir \"c\" para continuar : "))