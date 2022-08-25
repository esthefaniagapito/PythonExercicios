# Fazer a leitura de um número real e exibir apenas a parte inteira

import math

numero_real = float(input('Enter a number:'))
print('O número {} sem as casas decimais é {}'.format(numero_real, math.trunc(numero_real)))
