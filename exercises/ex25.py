# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Km/h: '))
multa = (velocidade - 80) * 7.0

if velocidade > 80:
    print('Você ultrapassou o limite de 80km/h, multa de R${:.2f}'.format(multa))
else:
    print('Você está abaixo da velocidade permitida')
