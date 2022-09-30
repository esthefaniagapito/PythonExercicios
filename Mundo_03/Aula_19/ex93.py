"""
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
nome = str(input('Nome do jogador: '))
num_partidas = int(input('Número de partidas: '))
lista_gols = list()

for i in range(1, num_partidas + 1):
    gols_x = int(input(f'Na partida {i} fez: '))
    lista_gols.append(gols_x)

aproveitamento = {
    'jogador': nome,
    'partidas': num_partidas,
    'gols': lista_gols,
    'total': sum(lista_gols)
}
print(aproveitamento)
print('-='*30)
for i, v in aproveitamento.items():
    print(f'O campo {i} tem valor {v}.')
print('-='*30)
print(f'O jogador {aproveitamento["jogador"]} jogou {len(aproveitamento["gols"])} partidas.')
for i, v in enumerate(aproveitamento['gols']):
    print(f'  => Na partida {i}, fez {v} gols.')
print(f'Foi um totoal de {aproveitamento["total"]} gols.')