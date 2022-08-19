# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

price = float(input('Digite the price of a product: US$'))
discount = price * 0.05
new_price = price - discount

print('For US${:.2f} your discount is US${:.2f}, so the new price is US${:.2f}.'.format(price, discount, new_price))