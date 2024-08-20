import sys
monto = int(sys.argv[1])
if len(sys.argv)<=2:
    #print("sin argumento")
    menor="mayor"
else:
    if sys.argv[2]!="menor":
        print("Lo sentimos, no es una operación válida")
        menor="d"
    else:
        menor = sys.argv[2]
precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}
def filtro():
    if menor=="menor":
        print("los productos menores al umbral son: ")
        for k,v in precios.items():
            valor=v
            if valor<monto:
                print(k)
    elif menor=="mayor":
        print("los productos mayores al umbral son: ")
        for k,v in precios.items():
            valor=v
            if valor>monto:
                print(k)

filtro()