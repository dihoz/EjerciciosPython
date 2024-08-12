import os
import colorama
#dic = dict([("a",1),("b",2)])
#print(dic)
#lista=list({"k":5,"k2":7}.items())
#print(lista)
os.system("cls")
promedio=[]
curso=[]
curso.append({"rut":"1-1","n1":1.0,"n2":5.5,"n3":7})
curso.append({"rut":"2-2","n1":4.0,"n2":7.0,"n3":4.0})
curso.append({"rut":"1-1","n1":2.0,"n2":3.5,"n3":3.9,"n4":4.5})
prueba=0
sumaglobal=0
cont=0
contglobal=0
#print(curso)
for x in curso:
    for k,v in x.items():
        if k!="rut":
            prueba += v
            cont+=1
            contglobal+=1
            #print(prueba)
            sumaglobal+=v
        else:
            rut=(v)
    promedio_alumno=prueba/cont
    if promedio_alumno>=3.95:   
        estado="aprobado"
        print(colorama.Fore.WHITE+f"El promedio del alumno {rut} es : {promedio_alumno} y está {colorama.Fore.GREEN+estado}")
    else:
        estado="reprobado"
        print(colorama.Fore.WHITE+f"El promedio del alumno {rut} es : {promedio_alumno} y está {colorama.Fore.RED+estado}")
    prueba=0
    cont=0
print("------------------------------")
promedio= sumaglobal/contglobal
print(colorama.Fore.WHITE+"el promedio global es : ",promedio )
