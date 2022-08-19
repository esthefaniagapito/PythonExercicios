# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Km: '))
days = int(input('Days: '))
rental = (km * 0.15) + (days * 60)

print('For {}km during {} days it costs US${:.2f} to rental a car.'.format(km, days, rental))