# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# pra de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list

pessoa = {
    'nome': 'Gabriel',
    'sobrenome': 'Murai',
    'idade': 21,
    'altura': 1.70,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 456},
    ]
}
print(pessoa['nome'])
print(pessoa['sobrenome'])
print(pessoa['idade'])
print(pessoa['altura'])
print(pessoa['endereços'])

print()

for dados in pessoa:
    print(dados, pessoa[dados])

