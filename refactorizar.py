def cuadrado_cubo(valor):
 return valor**2 + valor**3

def mult_234(valor):
 return valor*2 + valor*3 + valor*4
"""
valor_entrada = 2
valor_1 = cuadrado_cubo(valor_entrada)
print("valor 1", valor_1)
valor_2 = mult_234(valor_1)
print("valor 2", valor_2)
valor_3= cuadrado_cubo(valor_2)
print("valor 3", valor_3)
valor_4 = mult_234(valor_3)
print("valor 4", valor_4)
valor_5 = cuadrado_cubo(valor_4)
print("valor 5", valor_5)
valor_6 = mult_234(valor_5)
print("valor 6", valor_6)
"""
def op_combinada(valor):
 var_intermedia = cuadrado_cubo(valor)
 return mult_234(var_intermedia)
def compose(f, n):
    def fn(x):
        for _ in range(n):
            x = f(x)
            print(x)
        return x
    return fn
valor_entrada = 10
valor_6 = compose(op_combinada, 3)(valor_entrada)
print("final",valor_6)