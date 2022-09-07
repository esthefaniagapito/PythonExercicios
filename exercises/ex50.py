# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.

from datetime import date
qtd_pessoas = 0
atual = date.today().year
for i in range(0, 7):
    ano_nascimento = int(input('Ano nascimento: '))
    idade = atual - ano_nascimento
    if idade >= 18:
        qtd_pessoas += 1
print(qtd_pessoas)