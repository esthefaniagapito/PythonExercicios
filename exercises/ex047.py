# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
a1 = int(input('Digite A1: '))
r = int(input('Digite a razão: '))
an = a1 + (10 - 1) * r
for i in range(a1, an + r, r):
    print('{}'.format(i), end=' >> ')
print('Acabou!')
