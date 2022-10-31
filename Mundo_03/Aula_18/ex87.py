"""
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
 A) A soma de todos os valores pares digitados.
 B) A soma dos valores da terceira coluna.
 C) O maior valor da segunda linha.
"""

# Guanabara
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
        for c in range(0, 3):
                matriz[l][c] = int(input(f'Digite um valor [{l}], [{c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
            print(f'[{matriz[l][c]:^5}]', end='')
    print()

# Minha resolução
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = []
for l in range(0, 3):
        for c in range(0, 3):
                valor = int(input(f'Digite um valor [{l}], [{c}]: '))
                matriz[l][c] = valor
                if valor % 2 == 0:
                    par.append(valor)
for l in range(0, 3):
    for c in range(0, 3):
            print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'Lista par: {par}')

#Resolução do Guanabara
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c] # pegando o primeiro elemento na linha
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}.')

