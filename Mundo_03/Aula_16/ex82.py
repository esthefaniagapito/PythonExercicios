"""
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""

lista6 = []
listapar = []
listaimpar = []

for i in range(0, 5):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    lista6.append(n)
print(f'Os valores digitados foram {lista6}.')
print(f'Os valores digitados para lista par foram {listapar}.')
print(f'Os valores digitados para lista ímpar foram {listaimpar}.')

