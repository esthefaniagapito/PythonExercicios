# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres
# têm menos de 20 anos.

somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulheres = 0
for i in range(1, 5):
    print('------{}° PESSOA -------'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]:')).strip()
    somaidade += idade
    if i == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn'and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulheres += 1
médiaidade = somaidade / 4
print('A média da idade do grupo é de {} anos'.format(médiaidade))
print('O Homem mais velhor do grupo tem {} e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres no grupo'.format(totmulheres))
