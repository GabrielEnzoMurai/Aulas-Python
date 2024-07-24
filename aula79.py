"""
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iteráveis com  as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave especificada (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro
Se criar chaves iguais no dicionário o len não conta
as repetidas.
"""
pessoa = {
    'nome': 'Gabriel Enzo',
    'sobrenome': 'Murai',
    'idade': 21,
}

pessoa.setdefault('idade', None)
print(pessoa['idade'])
print(len(pessoa)) #__len__()
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))

for chave in pessoa:
    print(chave)

print(20 * '*')

for valor in pessoa.values():
    print(valor)

print(20 * '*')

for chave, valor in pessoa.items():
    print(chave, valor)
