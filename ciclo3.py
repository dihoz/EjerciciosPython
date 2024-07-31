import os
import colorama
os.system("cls")
print(colorama.Fore.GREEN+"----------------- Nacionalidad ------------------------\n")
salir="S"
conteo_chileno=0
conteo_extranjero=0
while salir!="N":
    nacionalidad=int(input(colorama.Fore.WHITE+"Por favor ingrese la nacionalidad (1-Chilena, 2-Extranjero) : "  ))
    if nacionalidad==1:
        conteo_chileno += 1
    elif nacionalidad==2:
        conteo_extranjero += 1
    else:
        print("valor no valido\n")
    salir = input(colorama.Fore.LIGHTRED_EX+"desea continuar s/n ").upper()
print(colorama.Fore.WHITE+f"La cantidad de chilenos es {conteo_chileno}")
print(f"la cantidad de extranjeros es {conteo_extranjero}")
if conteo_extranjero==0:
    print("la proporción de chilenos vs extranjeros es 100 porciento chilenos")
else:
    print("la proporción de chilenos vs el total es ",conteo_chileno/(conteo_chileno+conteo_extranjero)*100, "%")
    print("la proporción de chilenos vs extranjeros es ",conteo_chileno/conteo_extranjero)