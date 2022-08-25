# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome_completo = 'Maurício Dias Silva'
print(nome_completo.upper()) # 1
print(nome_completo.lower()) # 1
total_letras = len(nome_completo) - nome_completo.count(' ')
print(total_letras) # 2
primeiro_espaco = nome_completo.split()
print(nome_completo[0:len(primeiro_espaco[0])])
