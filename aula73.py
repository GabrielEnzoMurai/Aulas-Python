# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável
def multiplica(*args):
    total_multiplicacao = 1
    for numero in args:
        total_multiplicacao *= numero
    return total_multiplicacao

print(multiplica(1, 2, 4))


# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar

def par_impar(numero):
    if numero % 2 == 0:
        return f'O número {numero} é par'
    return f'O número {numero} é ímpar'
    
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))