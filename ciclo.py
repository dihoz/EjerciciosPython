#ejercicio de ciclo y algo mas
import os
import getpass
import colorama
os.system("cls")
f=open("ciclo_log.txt","at")
print(colorama.Fore.GREEN+"---------------   BILLETERA ELECTRONICA -----------------")
usuario = str(input(colorama.Fore.WHITE+"ingrse su usuario : "))
password = getpass.getpass('Ingrese un Password: ')
billetera = int(input("ingrese el saldo inicial de la billetera : "))
f.write("usuario,"+usuario+",")
f.write("pass,"+password+",")
f.write("saldo,"+str(billetera)+",")
continuar="S"
while billetera>0 and continuar=="S":
    gasto_desc=str(input("ingrese la descripción del gasto : "))
    gasto_desc=gasto_desc+","
    f.write(gasto_desc)
    gasto_monto=str(input("ingrese el monto del gasto : "))
    gasto_monto=gasto_monto+"\n"
    f.write(gasto_monto)
    if int(gasto_monto)<=billetera: #and gasto_monto%5000==0:
        billetera -= int(gasto_monto)
        print(f"gastaste {gasto_monto} y te queda {billetera}")
    else:
        print("Saldo insuficiente")
    continuar=input("desea continuar s/n").upper()
f.close()
f = open("ciclo_log.txt","r")
print(f.read())
f.close()
#import os
#os.remove("ciclo_log.txt")