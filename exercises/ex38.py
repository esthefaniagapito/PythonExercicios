# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#
# – EQUILÁTERO: todos os lados iguais
#
# – ISÓSCELES: dois lados iguais, um diferente
#
# – ESCALENO: todos os lados diferentes

l1 = float(input('L1: '))
l2 = float(input('L2: '))
l3 = float(input('L3: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os seguimentos podem formar um triângulo')
    if l1 == l2 == l3:
        print('EQUILÁTERO')
    elif l1 != l2 != l3:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos não podem formar um triângulo')