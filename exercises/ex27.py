# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 parta viagens mais longas.

km = float(input('Digite a distância: '))
p1 = km * 0.5
p2 = km * 0.45

if km <= 200:
    print('O valor da viagem é R${:.2f}'.format(p1))
else:
    print('O valor da viagem é R${:.2f}'.format(p2))