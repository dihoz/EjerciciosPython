#import random
#x= random.randrange(1,10)
from random import randrange as rr
lista=[rr(1,10) for x in range(5)]
print(lista)