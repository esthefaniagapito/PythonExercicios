# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.

# Primo = divisível apenas por 1 e o próprio número


n = int(input('Número: '))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
if count == 2:
    print('PRIMO!')
else:
    print('Não é primo!')