# Manipulando string

phrase = 'curso em vídeo Python'
print(len(phrase)) # tamanho da string
print(phrase.count('o')) # 3 letras o
print(phrase.find('v')) # retorna o índice da letra procurada
print(phrase.replace('Python','Android')) # modifica um termo na string
print(phrase.upper()) # maiúsculo
print(phrase.lower()) # minúsculo
print(phrase.capitalize()) # deixa apenas a primeira letra em maiúsculo
print(phrase.title()) # deixa todas as primeiras letras em maiúsculo
print(phrase.strip('Python'))

name = 'Silvio Morais'
print(len(name))
print(name[0:6]) # a partir do índice zero até o 6
print(name[-6:-1])
print(name[0::]) # a partir do zero sem limite final
print(name[-13::]) # idem acima, mas de trás pra frente
print(name[4:-4])

# utilizando aspas triplas

texto = '''Este é Silvio Morais,
uma pessoa que estuda à noite e 
trabalha de dia.
'''
print(texto)

# testando o método strip, que exclui espaços no início e
# no final da string
trecho = '   Modelo de trecho com espaços   '
print(len(trecho)) # output: 34
novo_trecho = trecho.strip()
print(len(novo_trecho)) # 28, removeu 3 espaços no início e no fim
