# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite seu salário: R$'))

aumento_10 = ((salario * 0.10) + salario)
aumento_15 = ((salario * 0.15) + salario)

if salario > 1250:
    print('Você recebeu um aumento de {}'.format(aumento_10))
else:
    print('Você recebeu um aumento de {}'.format(aumento_15))