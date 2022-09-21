"""
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
"""
tabela_times = ('Palmeiras', 'Santos', 'Vasco', 'Grêmio', 'Flamenggo',
                'Corinthians', 'Internacional', 'Cruzeiro', 'São Paulo',
                'Atlético', 'Botafogo', 'Fluminense', 'Coritiba', 'Bahia',
                'Goiás', 'Guarani', 'Sport', 'Portuguesa', 'Atlético Paranaense',
                'Vitória')
# Os 5 primeiros times.
print('='*40)
for pos, time in enumerate(tabela_times[0:6]):
    print(f'O time na posição {pos} é {time}.')

print('='*40)
# Os últimos 4 colocados.
for cont in tabela_times[16:]:
    print(f'Os últimos 4 colocados são: {cont}')

print('='*40)
# Times em ordem alfabética
print(sorted(tabela_times))

print('='*40)
# Em que posição está o time da Chapecoense.
if tabela_times.__contains__('Chapecoense'):
    print(tabela_times.index('Chapecoense'))
else:
    print('Time não classificado!')