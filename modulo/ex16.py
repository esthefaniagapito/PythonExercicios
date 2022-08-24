# Faça a leitura de um ângulo qualquer e exiba seu seno, conseno e tangente

import math

angulo = float(input('Digite um ângulo:'))
print('O seno de {} é {}'.format(angulo, math.sin(angulo)))
print('O conseno de {} é {}'.format(angulo, math.cos(angulo)))
print('A tangente de {} é {}'.format(angulo, math.tan(angulo)))