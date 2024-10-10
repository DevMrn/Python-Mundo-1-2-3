"""Escreva um programa que leia a velocidade de um carro.
    Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
    A multa vai custar R$7,00 por cada Km acima do limite."""

velocidade = int(input('Velocidade atual do carro: '))

if velocidade > 80:
    multa = (velocidade-80) * 7
    print('Multado! Você excedeu o limite de 80Km/h')
    print(f'Você deve pagar R${multa:.2f}!')
print('Tenha um bom dia! Diriga com segurança!')
