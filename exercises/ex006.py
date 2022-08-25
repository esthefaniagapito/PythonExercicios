# Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros.

meters = int(input('Enter a number:'))
meters_to_cm = meters * 100
meters_to_mm = meters * 1000

print('{} meters is {}cm and is {}mm'.format(meters, meters_to_cm, meters_to_mm))