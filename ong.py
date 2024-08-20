def factorial(numero):
    numero=([x+1 for x in range(numero)])
    fact=1
    for y in range(len(numero)):
        fact*=numero[y]
    return fact
def  productoria(lista):
    fact=1
    for y in range(len(lista)):
        fact*=lista[y]
    return fact
def calcular(**x):
    for k,v in x.items():
        if type(v)!=list:
            print(factorial(v))
        else:
            print(productoria(v))

a = [3, 6, 4, 2, 8]

print(factorial(5))
print(productoria(a))
calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6, fact_3=9)
