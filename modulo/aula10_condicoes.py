nome = str(input('Qual é o seu nome?'))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
print('Bom dia, {}!'.format(nome))

print('##########')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = n1 + n2 / 2
print('A sua média foi {:.2}'.format(m))
if m >= 6:
    print('Parabéns, vc passou')
else:
    print('Sua média foi ruim, estude mais!')

# outra forma
print('Parabens' if m >= 6 else 'estude mais')
