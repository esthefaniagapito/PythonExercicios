"""
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
"""
maiorde18 = 0
homens = 0
mulheres = 0
while True:
    idade = int(input('Digite idade: '))
    sexo = str(input('Digite o sexo [F/M]: ')).strip().upper()[0]
    if idade > 18:
        maiorde18 += 1
    elif sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres += 1
    resposta = str(input('Gostaria de cadastrar novo usuário [S/N]? ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'O total de pessoas com mais de 18 anos é de {maiorde18}')
print(f'O total de homens é de {homens}')
print(f'O total de mulheres com menos de 20 anos é de {mulheres}')