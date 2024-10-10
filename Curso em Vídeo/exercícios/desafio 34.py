"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
    Para salários superiores a R$1250,00, calcule um aumento de 10%.
    Para os inferiores ou iguais, o aumento é de 15%."""

salario = float(input('Salário do funcionário: '))

if salario <= 1250:
    novo = salario + (salario*15/100)
else:
    novo = salario + (salario*10/100)
print(f'Salário antigo: R${salario:.2f}')
print(f'Salário novo: R${novo:.2f}')
