# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo:')).strip()
partes_do_nome = nome.split()
print('Seu primeiro nome é {} e seu último nome é {}'.format(partes_do_nome[0], partes_do_nome[-1]))