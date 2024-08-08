import random
valores3=[int(random.random()*200) for x in range(7)]
print(valores3)

divisibles = []
for valor in valores3:
    if valor % 2 == 0 :
        divisibles.append('Divisible')
    else:
        divisibles.append('No Divisible')
print(divisibles)

print(["Divisible" if x%2==0 else "No Divisible" for x in valores3])

valores2=[int(random.random()*200) for x in range(10)]
print(valores2)
nuevalista = [x if x%5==0 else 0 for x in valores2]
print(nuevalista)

print([x if x%5==0 or x>50 else 0 for x in [int(random.random()*200) for x in range(10)]])

lista = ['Lechugas', 'Tomates', 5, 10,
 True, False, True, 'Papas',
 5.1, 45.2, 1, 2, 0]
count_str = 0
for elemento in lista:
    if type(elemento) is not str:
        count_str += 1
print(count_str)

lst_str = [elemento for elemento in lista if type(elemento) is str ]
print(len(lst_str))
print("----------------------------------------------------------")

claves = ['nombre','apellido','edad','altura']
valores = ['Juan','Pérez', 33, 1.75]
print({k:v for k,v in zip(claves, valores)})

print({k:v for k,v in zip(valores3,divisibles)})

a = [100, 200, 1000, 5000, 10000, 10, 5000]
n = len(a)
filtered_array = []
for i in range(n):
    if a[i] >= 1000:    
        filtered_array.append(a[i])
print(filtered_array)

filtro2 = [x for x in a if x >= 1000]
print(filtro2)

filtro3 = [ x if x>=1000 else None for x in a]
print(filtro3)

seconds = [100,50,1000,5000,1000,500]
minutos = [str(str(x//60)+":"+str(x%60)) for x in seconds]
print(minutos)

paises=["México","Chile","Argentina"]
cant_usu=[70,50,55]
dic={k:v for k,v in zip(paises, cant_usu)}
dic_f={k:v for k,v in zip(paises, cant_usu) if v<60}
print(dic_f)

mes=["oct","nov","dic"]
ventas=(65000,68000,72000)
dict_ventas={k:v for k,v in zip(mes,ventas)}
print(dict_ventas)
dict_venta_10porc={k:v*1.1 for k,v in zip(mes,ventas)}
print(dict_venta_10porc)
dict_venta_20porc={k:v*0.8 for k,v in zip(mes,ventas)}
print(dict_venta_20porc)
#dict_venta_20porc_2={k:v*0.8 for k,v in dict_venta_20porc}
#print(dict_venta_20porc_2)