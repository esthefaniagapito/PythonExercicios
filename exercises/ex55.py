# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

a1 = int(input('Digite a1: '))
r = int(input('Digite a razão: '))
termo = a1
count = 1

while count <= 10:
    print('{} -> '.format(termo), end=' ')
    termo += r
    count += 1
print('FIM!')

