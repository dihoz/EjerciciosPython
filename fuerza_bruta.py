from string import ascii_lowercase
import getpass
abc = ascii_lowercase
y=0
contador=0
clave = getpass.getpass('Ingrese un Password: ') 
for x in range(len(clave)):
    z=0
    while z!=-1:
        contador += 1
        if clave[x]==abc[y]:
            y = 0
            z=-1
        else:
            y += 1
print("La cantidad de intentos es : ",contador)


veces = 0
for letra in clave:
    for caracter in abc:
        veces+=1
        if letra == caracter:
            break
print ("intentos : ",veces)