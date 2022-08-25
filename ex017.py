# Leia uma lista de nomes e exiba a sua ordem

import random

nome_01 = input('Nome 01:')
nome_02 = input('Nome 02:')
nome_03 = input('Nome 03:')
nome_04 = input('Nome 04:')

lista_de_alunos = [nome_01, nome_02, nome_03, nome_04]
random.shuffle(lista_de_alunos)

print('A ordem de apresentação é')
print(lista_de_alunos)