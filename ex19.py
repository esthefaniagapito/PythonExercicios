# Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos dígitos separados.

valor = int(input('Digite um número:'))
unidade = valor // 1 % 10
dezena = valor // 10 % 10
centena = valor // 100 % 10
milhar = valor // 1000 % 10

print('''
Unidade: {}
Dezana: {}
Centena: {}
Milhar: {}
'''.format(unidade, dezena, centena, milhar))