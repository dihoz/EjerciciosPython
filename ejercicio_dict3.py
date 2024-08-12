curso={ "1-1":[],
        "2-2":[],
        "3-3":[]
      }
print("notas del curso")
for k,v in curso.items():
    print(k,v)

while True:
    rut=input("ingrese el rut :")
    if rut not in curso.keys():
        print("El rut no existe")
    else:
        if len(curso[rut])<3:
            #print(len(curso[rut]))
            nota=float(input("ingrese la nota : "))
            curso[rut].append(nota)
        else:
            print("no puede ingresar mas notas")
    sigue = input("Desea continuar s/n").upper()
    if sigue!="S":
        break
for k,v in curso.items():
    if len(v) >0:
        print(f"El rut {k} tiene {v} notas, el promedio es {sum(v)/len(v):.2f} y su estado es {"aprobado" if sum(v)/len(v)>=3.95 else "reprobado"}")
    else:
        print(f"El alumno {k} no tiene notas")