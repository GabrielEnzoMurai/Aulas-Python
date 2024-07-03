# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2 ,3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    ['Maria', 'Helena', ],
    ['Elaine', ],
    ['Luiz', 'João', 'Eduarda', ],
]

# p , *_, b = lista
# print(p, b)

# for nome in lista:
#     print(nome, end = " ")
    
# print('\n')
# print(*lista)
# print(*string)
# print(*tupla)
print(*salas, sep = '\n')

