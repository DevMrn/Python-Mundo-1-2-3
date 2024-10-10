"""Desenvolva um programa que pergunte a distância de uma viagem em Km.
    Calcule o preço da passagem,cobrando R$0,50 por Km para viagens de até 200Km
    E R$0,45 parta viagens mais longas."""

distancia = int(input('Distância da viagem: '))
print('\n')

if distancia <= 200:
    preco = distancia*0.50
    print(f'Distância: {distancia:.1f}Km')
    print(f'Preço: R${preco:.2f}')
else:
    preco = distancia*0.45
    print(f'Distância: {distancia:.1f}Km')
    print(f'Preço: R${preco:.2f}')
