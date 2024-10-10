# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))

# Menor
if v1 < v2 and v1 < v3:
    print(f'O menor valor foi: {v1}')
elif v2 < v1 and v2 < v3:
    print(f'O menor valor foi: {v2}')
else:
    print(f'O menor valor foi: {v3}')

# Maior

if v1 > v2 and v1 > v3:
    print(f'O maior valor foi: {v1}')
elif v2 > v1 and v2 > v3:
    print(f'O maior valor foi: {v2}')
else:
    print(f'O maior valor foi: {v3}')
