import sys
if len(sys.argv)<2:
    print("Falta argumento")
    
else:
    ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
    }

    print ({k:v for k,v in ventas.items() if v>int(sys.argv[1])})


