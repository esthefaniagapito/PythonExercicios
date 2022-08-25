# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece
# a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

a = str(input('Digite algo: ')).upper()
print('O input possui {} letras A'.format(a.count('A')))
print('A primeira letra A está na posição {}'.format(a.find('A')+1))
print('A última letra A está na posição {}'.format(a.rfind('A')+1))