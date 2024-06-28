"""
Iterando strings com while
"""
#       0123456789101112
nome = 'Helena Sekiguti' #Iteráveis
#       121110987654321
numero = 0
novo_nome = ''

while numero < len(nome):
    letra = nome[numero]
    novo_nome += f'*{letra}'
    numero += 1

novo_nome += '*'
print(novo_nome)



