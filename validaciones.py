"""
Para poder ingresar notas debe primero ingresar una password, al
tercer intento el usuario es bloqueado y debe emitir un mensaje
indicando que superó los tres intentos.
clave = "VamosConTodo"

EL programa debe permitir el ingreso de 5 notas validadas en el rango
Se debe imprimir el promedio una vez que finalice el programa

v2.0 Indicar cuál fue la menor y la mayor nota ingresada durante el proceso

"""

import os
import colorama
import getpass
#password="VamosConTodo"
os.system("cls")
ciclo=3
suma=0
promedio=0
notamax=0
notamin=7
print(colorama.Back.GREEN + colorama.Fore.YELLOW+"---------------------------------------------------------------------------------------")
print("                             SISTEMA DE REGISTRO DE NOTAS                              ")
while ciclo>0:
    password=getpass.getpass(colorama.Fore.GREEN+colorama.Back.BLACK+'Ingrese un Password: ')
    if password=="VamosConTodo":
        ciclo=0
        for x in range(5):
            while True: 
                nota = float(input(colorama.Fore.LIGHTBLUE_EX+f"ingrese la nota {x+1} :"))
                if nota >= 1 and nota <=7:
                    print(colorama.Fore.GREEN+"nota ingresada ok")
                    suma+=nota
                    promedio= suma/5
                    if nota>notamax:
                        notamax=nota
                    if nota<notamin:
                        notamin=nota
                    break   
                else:
                    print(colorama.Fore.RED+"error en nota")
        print(colorama.Fore.WHITE+"El promedio es : ",promedio)
        print("La nota máxima es : ",notamax)
        print("La nota mínima es : ",notamin)
        if promedio>=3.95:
            print(colorama.Fore.GREEN+"el alumno está aprobado")
        else:
            print(colorama.Fore.RED+"el alumno está reprobado")
    else:
        print(colorama.Fore.LIGHTRED_EX+ f"intentelo denuevo, le quedan {ciclo-1} intentos")
        ciclo-=1

    
        
    