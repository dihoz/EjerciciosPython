"""
x = float(input("ingrese valor 1 : "))
y = float(input("ingrese valor 2 : "))
if x>y:
    print("la suma es :", x+y)
elif x==y:
    print("la multiplicación es : ", x*y)
else:
    for x in range(1,11):
        print(f"la multiplicación de {x} por {y} es {x*y}")
"""

while True:
    x = float(input("ingrese valor mayor a 10  : "))
    if x>10:
        print("gracias")
    else:
        for y in range(5):
            print("error")
    z=input("desea continuar y/n")
    if z!="y":
        break