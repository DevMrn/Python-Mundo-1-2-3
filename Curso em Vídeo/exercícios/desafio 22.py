"""Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome."""

nome = str( input("Digite seu nome completo: ")).strip()

print('Em letras maiuscúlas: {}'.format(nome.upper()))
print('Em letras minuscúlas: {}'.format(nome.lower()))
print('Total de caracteres: {}'.format(len(nome) - nome.count(' ')))

lista = nome.split()

print('Seu primeiro nome é {} e ele tem {} letras.'.format(lista[0], len(lista[0])))