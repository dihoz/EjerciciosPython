'''
Dados los lados A y B de un triángulo rectángulo, según el Teorema de Pitágoras, el cuadrado de la hipotenusa (C), 
es igual a la suma del cuadrado de los catetos (lados).
c2 = a2 + b2
Elaborar un programa que lea el tamaño de los lados A y B, y calcule e imprima C (hipotenusa)
'''
class pitagoras():
    import math
    i="a"
    while i!="q":
        print("\n   -----          PITAGORAS         -----\n")
        print("   ----- Cálculo de triangulo rectángulo según el teorema de pitágoras   -----\n")
        #print(" Datos: \n Margen 20% \n IVA 19% \n")
        la=float(input("Ingrese el lado a : "))
        lb=float(input("Ingrese el lado b : "))
        resultado = math.sqrt(math.pow(la,2) + math.pow(lb,2))
        print(f"-------------------------------------\nEl valor del lado c es :{resultado:.2f}\n-------------------------------------")
        i=str(input("ingrese \"q\" para salir \"c\" para continuar : "))