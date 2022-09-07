# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:

# APOS A SOPA, A SACADA DA CASA,
# A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = input('Digite algo: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
# len(junto)-1 = número total de letras - 1, fica o total de índices
# - 1 (no meio) para ir até o última posição, que seria zero, mas temos que por -1
# -1 no final pq ele vai voltando uma letra, estamos de trás para frente.
for i in range(len(junto) -1, -1, -1):
# adicionando a frase invertida
    inverso += junto[i]
if inverso == junto:
    print('Temos um palindromo')
else:
    print('Não é um palindromo')