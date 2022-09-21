"""
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista5 = []
resposta = 'S'
tem5 = False
while resposta == 'S':
    n = int(input('Digite uma número: '))
    resposta = str(input('Gostaria de cadastrar outro número? [S/N] ')).strip().upper()[0]
    if resposta == 'S':
        lista5.append(n)
        for i in lista5:
            if i == 5:
                tem5 = True
    else:
        break
print(f'Os valores em ordem decrescente são {sorted(lista5, reverse=True)}')
print(f'O valor 5 foi digitado? Resposta: {tem5}')
