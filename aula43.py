# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_digitada != senha_salva:
#     senha_digitada = input(f'Coloque sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('O while de cima pode ser infinito')
# print('Senha correta!')

texto = 'Python'
novo_texto = ''

for letra in texto:
    novo_texto +=f'*{letra}'
    print(letra)


print(novo_texto + '*')

#for serve para funções que sabemos quantas repetições são necessárias