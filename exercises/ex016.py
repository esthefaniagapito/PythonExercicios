# Leia 4 nomes diferentes e sortei um deles
import random

nome_01 = input('Nome 01:')
nome_02 = input('Nome 02:')
nome_03 = input('Nome 03:')
nome_04 = input('Nome 04:')

lista_de_alunos = [nome_01, nome_02, nome_03, nome_04]

print('O aluno escolhido foi {}'.format(random.choice(lista_de_alunos)))