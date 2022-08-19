# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salary = float(input('Digit your salary: US$'))
salary_increase = salary + (salary * 15 / 100)

print('Your salary was US${:.2f} and with 15% of increase is now US${:.2f}'.format(salary, salary_increase))