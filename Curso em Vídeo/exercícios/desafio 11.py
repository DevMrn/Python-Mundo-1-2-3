# Faça um programa que leia a largura e a altura de uma parede em metros.
# Calcule a sua área e a quantidade de tinta necessária para pintá-la.
# Sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float( input('Digite a altura: '))
Alt = float( input('Digite a altura: '))
area = Alt * larg
tinta = area / 2

print('Sua dimensão é de {}x{} e sua área é de {}m².'.format(larg, Alt, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))