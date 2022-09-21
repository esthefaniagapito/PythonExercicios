"""
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""
from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os números sorteados: ', end='')
for i in n:
    print(f'{i}', end=' ')
print()
print(f'O menor número na lista é {min(n)}.')
print(f'O maior número na lista é {max(n)}.')

