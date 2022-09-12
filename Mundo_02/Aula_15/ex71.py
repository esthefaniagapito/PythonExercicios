"""
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
valor = int(input('Valor a sacar: R$'))
montante = valor
ced = 50
totalced = 0
while True:
    # Eu pego e montante, que é o valor a sacar e tento sacar dele R$50,00
    # se for possível eu retiro e conto a quantidade de vezes que isso foi feito
    # para saídas de R$50,00.
    if montante >= ced:
        montante -= ced
        totalced += 1
    # Se não der para tirar R$50,00 eu preciso verificar qual é a cédula atual
    # É 20, 10 ou 1?
    # E eu repito o processo acima, tirando a partir de 20 e assim sucessivamente
    # com as demais notas.
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        elif ced == 1:
            ced = 1
        totalced = 0
        if montante == 0:
            break
print('Volte sempre!')