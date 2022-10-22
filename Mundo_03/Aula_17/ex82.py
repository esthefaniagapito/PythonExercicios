"""
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""

lista = []
resposta = 'S'
lista_par = []
lista_impar = []
while resposta == 'S':
    n = int(input('Digite um número: '))
    resposta = str(input('Gostaria de inserir outro número? [S/N]: ')).strip().upper()[0]
    lista.append(n)
for i in lista:
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)
print(f'Lista completa: {lista}.')
print(f'Lista par: {lista_par}')
print(f'Lista ímpar: {lista_impar}')

