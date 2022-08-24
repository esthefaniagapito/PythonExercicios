import math
from math import sqrt
import emoji

num = int(input('Digite um número:'))
raiz = math.sqrt(num)
raiz2 = sqrt(num) # note que
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) # arredondando para cima
print('A raiz de {} é igual a {}'.format(num, sqrt(num)))

print(emoji.emojize('Hello, world :globe_with_meridians:'))
