"""
split e join com list e str
split - divide uma string
join - une uma string
Se não passar nenhum argumento no parentêses ele divide
pelos espaços
"""
frase = 'Olha só que, coisa interessante'
lista_palavras = frase.split(',')

for i, frase in enumerate(lista_palavras):
    lista_palavras[i] = lista_palavras[i].lstrip()

print(lista_palavras)

frases_unidas = ', '.join(lista_palavras)
print(frases_unidas)
