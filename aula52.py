"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
nome = 'Gabriel'
noutra_variavel = nome
nome = 'Murai'
print(noutra_variavel, nome)

lista_a = ['Gabriel', 'Murai', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
