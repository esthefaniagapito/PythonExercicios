"""
Exercício Python 085: Crie um programa onde o usuário possa digitar
sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares
e ímpares em ordem crescente.
"""
from typing import List

num = [[], []]
valor = 0
for i in range(1, 8):
    valor = int(input(f'Digite o {i} valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f'Todos os valores digitados foram {num}.')
print(f'Todos os valores pares digitados foram {num[0]}.')
print(f'Todos os valores ímpares digitados foram {num[1]}.')
