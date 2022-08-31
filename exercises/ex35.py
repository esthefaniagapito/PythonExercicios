# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano = int(input('Digite o ano de nascimento: '))
ano_base = 2022
idade = ano_base - ano

if idade == 18:
    print('Ano EXATO de alistamento')
elif idade > 18:
    print('Já se passou {} anos desde que você fez 18 anos'.format(idade - 18))
else:
    print('Não tem 18 anos ainda, não pode se alistar')