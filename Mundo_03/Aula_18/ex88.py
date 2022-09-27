"""
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

"""
O tamanho da minha lista, ou seja, quantos índices terão vai ser determinada
pela quantidade de jogos que o jogador que fazer.
Quero dois jogos, cada um com 6 números:
jogos = [[0, 0, 0, 0, 0, 0], [[0, 0, 0, 0, 0, 0]]

"""
from random import choices

num_disponiveis = list(range(1, 62))
qtd_num_por_jogo = 6
qtd_de_jogos = int(input('Quantos jogos deseja fazer: '))
lista_jogos_gerada = []

for _ in range(1, qtd_de_jogos + 1):
    lista_jogos_gerada.append(choices(num_disponiveis, k=qtd_num_por_jogo))
print(lista_jogos_gerada)

