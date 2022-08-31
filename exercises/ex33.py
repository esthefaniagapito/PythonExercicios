# Escreva um programa em Python que leia um número
# inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um número: '))
opcao = int(input('Digite 1 para binário, 2 para octal e 3 para hexadecimal: '))
binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)

if opcao == 1:
    print('O número {} em binário é {}'.format(numero, binario))
elif opcao == 2:
    print('O número {} em octal é {}'.format(numero, octal))
elif opcao == 3:
    print('O número {} em hexadecimal é {}'.format(numero, hexadecimal))