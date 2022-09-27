estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())  # a invés de estado[:]
print(brasil)
print('-=' * 35)
for e in brasil:
    for k, v in e.items(): # No caso de dicionários não há enumerate
        print(f'O campo {k} tem valor {v}.')
