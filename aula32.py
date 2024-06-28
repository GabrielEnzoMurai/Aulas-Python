"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreve "Seu nome é muito grande".
"""

#Ex 1

# numero_inteiro = input('Digite um número inteiro: ')

# if numero_inteiro.isdigit:
#     numero_inteiro_int = int(numero_inteiro)
#     par_impar_formula = numero_inteiro_int % 2 == 0
#     impar_par = 'ímpar'

#     if par_impar_formula:
#         impar_par = 'par'
        
#     print(f'O número {numero_inteiro_int} é {impar_par}')
    
# else:
#     print('Você não digitou um número inteiro')

# numero_inteiro = input('Digite um número inteiro: ')

# if numero_inteiro.isdigit():
#     numero_inteiro_int = int(numero_inteiro)
#     numero_par_impar = numero_inteiro_int % 2 == 0
        
#     if numero_par_impar:
#         print(f'O número {numero_inteiro_int} é par')
#     else:
#         print(f'O número {numero_inteiro_int} é ímpar')
# else:
#     print('Você não digitou um número inteiro')

#Ex 2

# entrada = input('Informe a hora: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     if entrada_int >= 0 and entrada_int <= 11:
#         print('Bom dia')
#     elif entrada_int >= 12 and entrada_int <= 17:
#         print('Boa tarde')
#     elif entrada_int >= 18 and entrada_int <= 23:
#         print('Boa noite')
#     else:
#         print('Você não digitou uma hora válida')
# else:
#     print('Digite apenas números inteiros')

#Ex 3 

primeiro_nome = input('Digite seu primeiro nome: ')

conta_letra = (len(primeiro_nome))

if conta_letra > 1:
    if conta_letra <= 4:
        print('Seu nome é curto')
    elif conta_letra >= 5 and conta_letra <= 6:
        print('Seu nome é normal')
    elif conta_letra > 6:
        print('Seu nome é muito grande')
else:
    print('Digite pelo menos uma letra')





