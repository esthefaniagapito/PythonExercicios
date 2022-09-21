"""
Exercício Python 079: Crie um programa onde o usuário possa digitar vários
valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro,
ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.
"""

lista3 = []
resposta = 'S'
while resposta == 'S':
    n = int(input('Digite um número: '))
    if n not in lista3:
        lista3.append(n)
    resposta = str(input('Gostaria de cadastrar outro número? [S/N] ')).strip().upper()[0]
list_crescente = sorted(lista3)
print(f'Os valores cadastrados na lista foram ', end='')
for i in list_crescente:
    print(f'{i} ', end='')