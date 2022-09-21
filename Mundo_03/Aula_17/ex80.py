"""
Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.
"""
lista4 = []
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > lista4[len(lista4) -1]:
        lista4.append(n)
    else:
        pos = 0
        while pos < len(lista4):
            # verificando se o número é menor ou igual ao número
            # atual na posição lista4[pos]
            if n <= lista4[pos]:
                lista4.insert(pos, n)
                break
            pos += 1
print(f'Os valores digitados foram {lista4}.')