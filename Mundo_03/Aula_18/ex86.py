"""
Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3
e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""
#Minha resolução
matriz = [[], [], []]
for i in range(0,3):
    matriz[0].append(int(input()))
    matriz[1].append(int(input()))
    matriz[2].append(int(input()))
for k, v in enumerate(matriz):
    print(f'{matriz[k]}')
    print()

# Guanabara
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
        for c in range(0, 3):
                matriz[l][c] = int(input(f'Digite um valor [{l}], [{c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
            print(f'[{matriz[l][c]:^5}]', end='')
    print()


