# Realizar a leitura de um número e exibir seu dobro, triplo e raiz quadrada

number = int(input('Enter a number:'))
double = number * 2
triple = number * 3
square_root = number**(1/2)

print('The double of {} is {}, its triple is {} and its square root is {:.2f}'.format(number, double, triple, square_root))
