# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

wallet_money = float(input('Type how much money you have in wallet: R$'))
dollar_today = 5.50
dollar_amount = wallet_money / dollar_today

print('You have in wallet R${} so it is possible to buy US${:.2f} dollars'.format(wallet_money, dollar_amount))
