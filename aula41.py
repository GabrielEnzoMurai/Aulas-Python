""" while/else """
# O else só é alcançado caso o while finalize
# Se encontrar um break no while o else não é executado
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]
    
    print(letra)
    i += 1
else:
    print('O else foi executado')
print('Fora do while')
