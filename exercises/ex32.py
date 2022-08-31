# escreva um programa para aprovar o empréstimo bancário para a compra
# de uma casa. O programa vai perguntar o valor da casa, o salário do comprador,
# e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
# o empréstimo será negado

casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do salário: R$'))
anos = int(input('Digite quanto anos para pagar: '))
prestacao = casa / (anos * 12)
limite = salario * 0.30

if prestacao >= limite:
    print('Empréstimo NEGADO')
else:
    print('Empréstimo CONCEDIDO!')
    print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos))
    print('O valor da prestação é de R${:.2f}'.format(prestacao))
