"""
Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
n = 0
total_n = 0
soma_n = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        soma_n += n
        total_n += 1
print('O total de números digitados foi de {} e a soma deles é de {}'.format(total_n, soma_n))
