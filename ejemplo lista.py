i="Y"
lista=[]
while i=="Y":
    elemento=input("Ingrese una palábra : ")
    if len(elemento)==0:
        print("Debe ingresar una palanbra")
    else:
        lista.append(elemento)
        i=input("Desea continuar Y/N: ").upper()
lista2=[len(x) for x in lista]
print(lista)    
print(lista2)
lista3= [x[::-1] if len(x)>5 else x for x in lista]
print(lista3) 
reversed(lista[0])
print(lista)