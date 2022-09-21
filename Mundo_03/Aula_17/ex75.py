"""
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
"""
n1 = int(input('N1: '))
n2 = int(input('N2: '))
n3 = int(input('N3: '))
n4 = int(input('N4: '))
tupla = (n1, n2, n3, n4)
cont = 0
index_de_3 = 0
lista_par = []
for i in tupla:
    if i == 9:
        cont += 1
    elif i == 3:
        index_de_3 = tupla.index(3)
    elif i % 2 == 0:
        lista_par.append(i)
print(f'O número 9 foi digitado {cont} vezes.')
print(f'O número 3 aparece em {index_de_3}.')
print(f'Os números pares são: {lista_par}.')