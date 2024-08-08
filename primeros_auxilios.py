print("-------------------------------------------")
print("           PRIMEROS AUXILIOS               \n")
print("Si está en una emergencia responda las siguintes preguntas, PERO RÁPIDO!!!!")
a = str(input("El afectado responde a estímulos? S/N : "))
if a.upper()=="S":
    print("Valore la necesidad de llevarlo al hospital mas cercano")
else:
    print(a)
    print("abrir la via aérea")
    b = str(input("respira? S/N : "))
    if b.upper()=="S":
        print("Permitirle posición de suficiente ventilación")
    else:
        print("Administrar 5 ventilaciones y llamar a la ambulancia")
        ambulancia_on = "N"
        while ambulancia_on=="N":
            c = str(input("Tiene signos de vida? S/N : "))
            if c.upper()=="S":
                print("Reevaluar la espera de la ambulancia")
                ambulancia_on=str(input("Llegó la ambulancia? S/N : "))
            else:
                print("Administrar compresiones torácicas hasta que llegue la ambulancia")
                ambulancia_on=str(input("Llegó la ambulancia? S/N : "))
                