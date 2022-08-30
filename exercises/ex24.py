import random

a = [0, 1, 2, 3, 4, 5]
b = int(input('Digite um número: '))
c = random.choice(a)

if b == c:
    print('Parabéns você acertou o número que eu estava pensando')
else:
    print('Você errou, eu estava pensando no número {}'.format(c))