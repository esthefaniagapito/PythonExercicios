# Criando primeira lista
teste = list() # ou []
teste.append('Gustavo')
teste.append(40)

# Criando segunda lista
galera = list()
galera.append(teste[:])  # [:] cria uma cópia
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])  # estou inserindo os novos itens
print(galera)

# Outra forma de declarar
galera2 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 22]]
print(galera2)

# Exibir os índices
print(galera2[0])  # ['João', 19]

# Primeiro índice e primeiro item
print(galera2[0][0])  # João

# Exibindo índice 1, item 1
print(galera2[1][1])  # 33

# Dentro de cada índice
for p in galera2:
    print(f'{p[0]} tem {p[1]} anos de idade.')

print()
# Fazendo inputs
galera3 = list()
dados = list()
totmai = tomen = 0
for c in range(0, 3):
    dados.append(str(input('Digite um nome: ')))
    dados.append(int(input('Idade: ')))
    galera3.append(dados[:])
    dados.clear()
print(galera3)

for p in galera3:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        tomen += 1
print(f'Temos {totmai} maiores de idade e {tomen} menores de idade.')

"""
Não confundor cópia de lista com ligação entre lista
"""
a = [1, 2, 3, 4]
b = a
b[2] = 8
print(a)
print(b)

"""
Out put: 
[1, 2, 8, 4]
[1, 2, 8, 4]

No exemplo acima estamos LIGANDO ambas a listas, logo se modificar uma afeta a outra.
Se b recebesse uma cópia de a[:], a permaneceria em seu estado original e apenas b, com
os dados copiados de a receberia 8 em b[2]. 
"""










