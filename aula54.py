"""
Exiba os índices da lista
"""
lista = ['Maria', 'Helena', 'Gabriel']
lista.append('João')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
    

    