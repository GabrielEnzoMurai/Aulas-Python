"""
Operação ternária (condição de uma linha)
<valor> if <condicao> else <outro valor>
"""
condicao = 10 == 10
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)

digito = 2
novo_digito = digito if digito <= 9 else 0
print(novo_digito)

print('Valor' if False else 'Outro valor' if True else 'Fim')