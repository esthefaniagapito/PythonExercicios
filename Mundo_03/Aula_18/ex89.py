"""
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média
de cada um e permita que o usuário possa mostrar as notas de cada
aluno individualmente.
"""

"""
Efetuar o cadastro de alunos até reposta negativa
"""
lista_alunos = list()

while True:
    nome = str(input('Nome: '))
    nota01 = float(input('Nota 01: '))
    nota02 = float(input('Nota 02: '))
    media = (nota01 + nota02) / 2
    lista_alunos.append([nome, [nota01, nota02], media])
    resp = str(input('Deseja cadastrar novos alunos? [S/N] ')).strip()[0]
    if resp in 'Nn':
        break
print('-='* 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for indice, alunos in enumerate(lista_alunos):
    print(f'{indice:<4}{alunos[0]:<10}{alunos[2]:>8.1f}')
while True:
    print('-='* 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opc == 999:
        print('Finanlizando')
        break
    if opc <= len(lista_alunos) -1:
        print(f'Notas de {lista_alunos[opc][0]} são {lista_alunos[opc][1]}')
    else:
        print('Registro não encontrado!')
print('<<<Volte sempre!>>>>')


