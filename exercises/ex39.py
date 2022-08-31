# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

import math
peso = float(input('PESO: '))
altura = float(input('ALTURA: '))
imc = peso / (altura ** 2)

print('O IMC é {}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= peso < 25:
    print('Peso ideal')
elif 25 <= peso < 30:
    print('Sobrepeso')
elif 30 <= peso < 40:
    print('Obesidade')
elif peso >= 40:
    print('Obsidade Mórbita')

