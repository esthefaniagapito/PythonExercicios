# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#
# 5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input('Número: '))
armazena = n
fatorial = 1
while armazena != 0:
    fatorial *= armazena
    armazena -= 1
print(fatorial)