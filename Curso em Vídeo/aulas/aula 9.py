# fatiamento

frase = 'Curso em Video Python'

print(frase[3]) # Do começo ao 3
print(frase[9:13]) # Do 9 até o 13
print(frase[:21]) # Do começo ao 21
print(frase[0:]) # Do 0 ao fim
print(frase[:]) # Do começo ao fim
print(frase[9:21:2]) # Do 9 até o 21 pulando de 2 em 2
print(frase[9::3]) # Do 9 até o fim pulando de 3 em 3
print(frase[::2]) # Do começo ao fim pulando de 2 em 2

frase = frase.replace('Python', 'Android') # Faz com que a string mude globalmente

# Análise

print(len(frase)) # Mostrar a quantidade de caracteres
print(frase.count('o')) # Conta quantas vezes aparece a letra 'o' minuscúla
print(frase.count('o,', 0, 13)) # Conta quantas vezes aparece a letra 'o' minuscúla, porém, com fatiamento
print(frase.find('deo')) # Indica em qual posição encontrou 'deo'
print('Curso' in frase) # Existe a palavra 'curso' na string frase?

# Transformação

print(frase.replace('Python', 'Android')) # Troca uma palavra, letra etc da string por outra mas apenas naquela instância
print(frase.upper()) # Deixa a string inteira com letras maiuscúlas
print(frase.lower()) # Deixa a string inteira com letras minuscúlas
print(frase.capitalize()) # Deixa a string inteira com letras minuscúlas menos a primeira letra
print(frase.title()) # Deixa a primeira letra de todas as palavras em maiuscúlo e o resto em minuscúlo
print(frase.strip()) # Remove todos os espaços inúteis no inicío e no fim da string -> EX. ('    Curso em Video Python   ')
print(frase.rstrip()) # Remove somente os últimos espaços da string, no caso o (r) significa Right
print(frase.strip()) # Remove somente os primeiros espaços da string, no caso o (l) significa Left

# Divisão

print(frase.split()) # Ele divide a string usando os espaços dela criando nova indexação a cada palavra

# Junção

print('-'.join(frase)) # Junta a string novamente usando oque estiver em aspas como espaço. EX -> 'C-u-r-s-o- -e-m- -V-i-d-e-o- -P-y-t-h-o-n'

# print(frase.upper().count('O')) resultaria em 3 pois upper deixou tudo em maiuscúlo