# Crie um programa que leia dois valores e mostre um menu na tela:
#
# [ 1 ] somar
#
# [ 2 ] multiplicar
#
# [ 3 ] maior
#
# [ 4 ] novos números
#
# [ 5 ] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.

import time

n1 = float(input('Valor 1: '))
n2 = float(input('Valor 2: '))
opcao = 0
while opcao != 5:
    print('''
    Escolha uma das opções:
    [ 1 ] somar

    [ 2 ] multiplicar

    [ 3 ] maior

    [ 4 ] novos números

    [ 5 ] sair do programa
    ''')
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('O maior valor é {}'.format(n1))
        else:
            maior = n2
            print('O maior valor é {}'.format(n2))
    elif opcao == 4:
        print('Insira novos valores!')
        n1 = float(input('Valor 1: '))
        n2 = float(input('Valor 2: '))
    elif opcao == 5:
        print('Saindo do programa...')
        time.sleep(2)
    else:
        print('Digite um valor válido!')
print('FIM!')