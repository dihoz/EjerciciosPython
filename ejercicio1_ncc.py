""""
Crear un algoritmo que permita ingresar los siguientes datos:
    cantidad de productos
    precio unitario
    departamento (1. Linea blanca, 2.Aseo y Limpieza 3.Refrigeración)
Si la cantidad de productos es mayor a 10 y corresponde al departamento de aseo y limpieza,
el total a pagar tiene un descuento del 8%

Cuando el producto es de refrigeración se debe agregar un 1% de recargo por concepto de 
traslado

Los productos de línea blanca están con un 20% de descuento pero el máximo 2 unidades por 
persona.

Al finalizar debe mostrar el detalle de los datos ingresados, los descuentos y/o recargos
correspondientes y el total a pagar por el cliente
    
"""
class productos():
    import os
    import math
    i="a"
    while i!="q":
        os.system("cls")
        print("\n   -----            INGRESE PRODUCTOS           -----\n")
        print("   ------------------------------------------------------\n")
        #print(" Datos: \n Margen 20% \n IVA 19% \n")
        cantprod=float(input("Ingrese la cantidad de productos : "))
        precio=float(input("Ingrese el precio unitario : "))
        depo=int(input("\n1.-Linea Blanca\n2.-Aseo y Limpieza\n3.-Refirgeración\nIngrese el número según corresponda al departamento: "))
        #resultado = math.sqrt(math.pow(la,2) + math.pow(lb,2))
        if depo==1:
            depo1="Linea Blanca"
        elif depo==2:
            depo1="Aseo y Limpieza"
        elif depo==3:
            depo1="Refrigeración"
        else:
            depo1="Otro Departamento"
        # asignación de descuentos
        descuento=0
        total=precio*cantprod
        if depo==2 and cantprod >10:
            precio2= precio*0.92
            descuento=precio*0.08*-1
            total=precio2*cantprod
        elif depo==3:
            precio2=precio*1.01
            descuento=precio*0.01
            total=precio2*cantprod
        elif depo==1 and cantprod<=2:
            precio2=precio*0.8
            descuento=precio*0.2*-1
            total=precio2*cantprod
        
        print(f"\nPara el producto del departamento {depo1}\ncon cantidad {cantprod} \nel precio unitario original es {precio}\nel descuento y/o recargo es {descuento}\n con un total a pagar de :{total}\n-------------------------------------")
        i=str(input("ingrese \"q\" para salir \"c\" para continuar : "))

productos()