# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Me diga qualquer número: '))
resultado = num % 2

if resultado == 0:
    print(f'O número {num} é PAR')
else:
    print(f'O número {num} é IMPAR')
