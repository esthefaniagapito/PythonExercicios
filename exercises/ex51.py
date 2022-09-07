# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

lista = []
for i in range(0, 5):
    peso = float(input('Digite seu peso: '))
    lista.append(peso)
print('O maior peso é {} e o menor é {}'.format(max(lista), min(lista)))
