"""
Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

# 1. Ler uma expressão
# 2. Remover os espaços em branco
# 3. Colocar em uma lista
# 4. Iterar sobre a lista e veriticar se é parênteses aberto
# Se for cont += 1
# 5. Na mesma iteração verificar se tem parênteses fechado
# Se houver cont +1
# 6. Se a quantidade de parenteses abertos for igual a quantidade de parênteses fehcados, então
# é uma expressão válida, não não é uma expressão válida.

expressao = str(input('Digite uma expressão: ')).strip()
lista = list(expressao)
parentese_aberto = 0
parentese_fechado = 0
for i in lista:
    if i == '(':
        parentese_aberto += 1
    elif i == ')':
        parentese_fechado += 1
if parentese_aberto == parentese_fechado:
    print('Expressão válida')
else:
    print('Expressão inválida')
