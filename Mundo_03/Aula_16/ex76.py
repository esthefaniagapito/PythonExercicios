"""
Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência. No final, mostre uma listagem de preços,
organizando os dados em forma tabular.
"""

tupla_produtos = ('café', 10.0,
                  'sabonete', 3.5,
                  'refrigerante', 4,
                  'cerais', 11)
for c in range(0, len(tupla_produtos)):
   if c % 2 == 0:
       print(f'{tupla_produtos[c]:.<30}', end='')
   else:
       print(f'R${tupla_produtos[c]:>7.2f}')





