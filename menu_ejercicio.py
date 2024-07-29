import os
import colorama
os.system("cls")
i="a"
while i!="q":
    print(colorama.Fore.GREEN+"MENU")
    print(colorama.Fore.LIGHTCYAN_EX+"-------------------------------\npara ingresar a IMPUESTO ingrese i")
    print("para ingresar a PITAGORAS ingrese p")
    print("para ingresar a IMC ingrese m")
    print(" para salir ingrese q\n-------------------------------")
    i=str(input(colorama.Fore.WHITE+"  -- :"))
    if i=="i":
        os.system("cls")
        import impuesto
        print(colorama.Fore.WHITE+"-")
        impuesto.impuesto()
    elif i=="p":
        os.system("cls")
        import pitagoras
        pitagoras.pitagoras()
    elif i=="m":
        os.system("cls")
        import imc
        imc.imc()
    