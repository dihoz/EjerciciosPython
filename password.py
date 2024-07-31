import getpass
# password = input('Ingrese un Password: ')
# también es posible resolver esto con getpass como sigue
# import getpass
password = getpass.getpass('Ingrese un Password: ')
if len(password) < 6:
    print('El password ingresado es demasiado corto')
