# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('-=-' * 10)
print('Analisador de Triângulos')
print('-=-' * 10)

r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima não podem formar um triângulo!')
