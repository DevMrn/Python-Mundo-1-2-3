# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = float( input('Digite o ângulo que deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O ângulo de {:.2f} tem o SENO de {:.2f}'.format(angulo,seno))
print('O ângulo de {:.2f} tem o COSENO de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {:.2f} tem o TANGENTE de {:.2f}'.format(angulo, tangente))