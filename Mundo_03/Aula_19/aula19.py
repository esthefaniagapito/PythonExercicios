# Dicionários
dados_A = dict()
dados_A = {'nome': 'Pedro', 'idade': 25}
print(dados_A['nome'])  # Output: Pedro
print(dados_A['idade'])  # Output: 25
print('-='*30)

# Adicionando elementos ao dicionário
dados_A['sexo'] = 'M'
print(dados_A)

print('-='*30)
# Removendo elementos
del dados_A['idade']
print(dados_A)

# Outro exemplo
print('-='*30)
filme = {
    'título': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}
print(filme.values()) # valores = conteúdo
print(filme.keys()) # as chaves dos valores
print(filme.items()) # pega ambos

print('-='*30)
for k,v in filme.items():
    print(f'O {k} é {v}')

print('-='*30)
locadora = [filme, filme, filme] # estou incluindo dicionários dentro da lista
print(locadora[1]['ano'])
locadora[1]['ano'] = 1995
print(locadora[1]['ano'])

