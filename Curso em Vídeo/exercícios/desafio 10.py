# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

saldo = float( input('Quanto você tem na carteira? R$'))
dolar = saldo / 5.23
euro = saldo / 5.70

print('\nCom R${:.2f} você pode comprar U${:.2f} e Є{:.2f}'.format(saldo, dolar, euro))