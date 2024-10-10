# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float( input('Qual é o salário do funcionário? R$'))
novo = salario + (salario * 15 / 100)

print('O funcionário ganhava R${:.2f}, com aumento de 15%, agora recebe R${:.2f}'.format(salario, novo))