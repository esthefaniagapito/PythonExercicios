"""
Aula 16 - Tuplas
"""
# Tuplas são imutáveis e são utilizadas para variáveis compostas
# Pode ser feito sem o lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)

# Pudim
print(lanche[3])

# Pizza
print(lanche[-2])

# Suco ... Pizza
print(lanche[1:3])

# Hambúrguer ... Suco
print(lanche[:2])

# Pizza, Pudim
print(lanche[2:])

# Suco, Pizza, Pudim
# Começa do ponto invertido e vai até o final
print(lanche[-3:])

"""
Preciso mainipular apenas o conteúdo, do jeito mais simples.
"""
print('=' * 30)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comida pra caramba!')
print('=' * 30)

"""
Preciso manipular o conteúdo também posso usar o range
que já havia sido estudado
"""
# Tamanho/comprimento da tupla = 4
print(len(lanche))
# O cont é o número do índice, se eu peço para exibir lanche[cont]
# estou pedindo para exibir da mesma forma o lanche[no_índice]
for cont in range(0, len(lanche)):
    print(lanche[cont])

print()
print('=' * 30)

"""
Caso além do conteúdo eu precise do index AINDA usando range
"""
# Preciso escrever a posição:
# Jeito simples:
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

"""
Preciso manipular o conteúdo e o index do jeito python: ENUMERATE
"""
# Utilizando enumarate
print('=' * 30)
for pos, comida in enumerate(lanche): # pos = posição (index), comida = (conteúdo)
    print(f'Eu vou comer {comida} na posição {pos}')

print('=' * 30)
# Método sorted (organizado)
print(sorted(lanche))
print(lanche)

print('=' * 30)
# Combinando tuplas
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
# (5, 8, 1, 2, 2, 5, 4)
print(c)
# Quantas vezes aparece o número 5?
# Out: 2
print(c.count(5))
# Em qual posição está 8?
# Out: 1, sempre a primeira ocorrência
print(c.index(8))
print('=' * 30)

# Combinar tipos diferentes
pessoa = ('Gistavo', 39, 'M', 99.88)
# Deleta a tupla inteira
# del(pessoa)
print(pessoa)

