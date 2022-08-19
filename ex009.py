# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e
# a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

width = float(input('Width: '))
height = float(input('Height: '))
area = width * height
tint = area / 2

print('You need {:.2f} liters of tint to paint a wall with {:.2f} of area'.format(tint, area))

