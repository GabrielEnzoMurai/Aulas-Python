# Manipulando chaves e valores em dicionários

pessoa = {

}

##
##

chave = 'nome'

pessoa[chave] = 'Gabriel Murai'
pessoa['sobrenome'] = 'Enzo'

print(pessoa[chave])

pessoa[chave] = 'Helena Sekiguti'

# del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])
