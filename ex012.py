# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Enter the temperature in celsius: '))
fahrenheit = ((celsius * 9)/5) + 32

print('{}°C are {}°F'.format(celsius, fahrenheit))