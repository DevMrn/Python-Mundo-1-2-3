n1 = int( input('Um valor: '))
n2 = int( input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {}, a divisão é {:.3f}'.format(s, m, d), end = '')
print(', a Divisão inteira é {} e a potência é {}'.format(di, e))

# end = ''  -  serve para continuar a linha

# Operadores aritiméticos