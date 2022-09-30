"""
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado
e tenham resultados aleatórios.Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor
tirou o maior número no dado.
"""
from random import randint
from time import sleep

jogo = {'jogador1': randint(1, 6),
        'joador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)
        }
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-='*35)
print(' == Ranking dos Jogadores ==')
num = 1
for i in sorted(jogo, key=jogo.get):
    print(f'{num}° lugar {i} com {jogo[i]}')
    num += 1
    sleep(1)

print()
# Segunda opção
ranking = list()
ranking = sorted(jogo.items(), key=jogo.get(1), reverse=True)
print('-='*30)
print('== Ranking dos Jogadores ==')
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)