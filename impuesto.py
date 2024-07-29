'''
Elaborar un programa que calcule e imprima el precio de venta de un artículo.
Se tienen los datos Descripción del artículo y costo de producción. El precio de venta se obtiene añadiendo al costo el 120% como utilidad y el 19% de impuesto.
'''

class impuesto():
    i="a"
    while i!="q":
        print("\n   -----          IMPUESTO         -----\n")
        print("   ----- Cálculo de precio de venta   -----\n")
        print(" Datos: \n Margen 20% \n IVA 19% \n")
        producto=str(input("Ingrese el nombre del producto : "))
        costo=float(input("Ingrese el costo de producción del producto : "))
        resultado = costo * 1.2 + costo * 0.19
        print(f"-------------------------------------\nEl precio del producto con IVA es :${resultado:.2f}\n-------------------------------------")
        i=str(input("ingrese \"q\" para salir \"c\" para continuar : "))
#impuesto()