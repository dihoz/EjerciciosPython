import os
import colorama
os.system("cls")
color=str(input("ingrese colores: verde, azul o rojo  "))
peso=float(input("ingrese valor entre 1 a 100 "))
if color.lower() == "verde" and peso >= 1 and peso <=100:
    print(colorama.Fore.GREEN+"ok")
elif color.lower() == "azul" and peso >= 1 and peso <=100:
    print(colorama.Fore.BLUE+"paso")
elif color.lower() == "rojo" and peso >= 1 and peso <=100:
    print(colorama.Fore.RED+"tamo")
else:
    print("error")
    