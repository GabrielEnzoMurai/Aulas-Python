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
p1 = {
    'nome': 'Gabriel',
    'sobrenome': 'Murai',
}
print(p1.get('nome', 'Não existe nome'))

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# p1.update({
#     'nome': 'Carlos',
#     'idade': 20,
# })
# p1.update(nome='Carlos',idade = 20)
# tupla = ('nome', 'Carlos'), ('idade', 20)
lista = [['nome', 'Carlos'], ['idade', 20]]
p1.update(lista)
print(p1)
