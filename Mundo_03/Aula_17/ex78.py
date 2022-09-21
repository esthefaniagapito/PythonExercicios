"""
Exercício Python 078: Faça um programa que leia 5 valores numéricos
e guarde-os em uma lista. No final, mostre qual foi o maior
e o menor valor digitado e as suas respectivas posições na lista
"""
# Primeira forma
lista1 = []
for i in range(0, 6):
    n = int(input('Digite um número: '))
    lista1.append(n)
print(f'O maior valor na lista é {max(lista1)} e sua posição é {lista1.index(max(lista1))}.')
print(f'O menor valor na lista é {min(lista1)} e sua posição na lista é {lista1.index(min(lista1))}.')

print('=' * 30)
# Segunda forma
lista2 = []
max = 0
min = 0
for j in range(0, 6):
    lista2.append(int(input('Digite um número: ')))
    if j == 0:
        max = min = lista2[j]
    else:
        if lista2[j] > max:
            max = lista2[j]
        if lista2[j] < min:
            min = lista2[j]
print(f'O maior valor na lista é {max} nas posições .',end='')
print(f'O maior valor na lista é {min} nas posições', end='')
for i, v in enumerate(lista2):
    if v == max:
        print(f'{i}...', end='')
print()
for i, v in enumerate(lista2):
    if v == min:
        print(f'{i}...', end='')
