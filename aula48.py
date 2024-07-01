"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    - append: Adiciona um item ao final
    - insert: Adiciona um item no índice escolhido
    - pop: Remove do final ou do índice escolhido
    - del: Apaga um índice
    - clear: Limpa a lista
    - extend: estende a lista
    - +: concatena listas
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)]
Evitar mover os índices da lista pq pode deixar lento o Python
"""


#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)

#        0     1     2               3     4
#       -5    -4    -3              -2    -1
lista = [123, True, 'Gabriel Murai', 1.2, []]
lista[-3] = 'Helena Sekiguti'
print(lista)
print(lista[2], type(lista[2]))




