"""
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
"""
total = preco = totalmaior1k = cont = menor = 0
produtobarato = ''
while True:
    produto = str(input('Produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    cont += 1
    if preco > 1000:
        totalmaior1k += 1
    if cont == 1:
        menor = preco
        produtobarato = produto
    else:
        if preco < menor:
            menor = preco
            produtobarato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Gostaria de cadastrar outro produto? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'O total gasto da compra é de R${total:.2f}.')
print(f'A quantidade de produtos maior de R$1000.00 é de {totalmaior1k}.')
print(f'O produto mais barato custa R${menor} e é o {produtobarato}')
