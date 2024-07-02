"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""
import os

lista_cliente = []

while True:
    opcoes_usuario = input ('Selecione uma opção\n'
                        '[i]nserir [a]pagar [l]istar: ')
   
    if opcoes_usuario == 'i':
        os.system('cls')
        inserir_lista = input('Insira um item na lista: ')
        lista_cliente.append(inserir_lista)
    
    elif opcoes_usuario == 'a':
        os.system('cls')
        excluir_lista = input('Escolha o índice que deseja apagar: ')
        try:
            indice = int(excluir_lista)
            del lista_cliente[indice]
        except:
            print('Não foi possível apagar esse índice')
    
    elif opcoes_usuario == 'l':
        os.system('cls')

        if len(lista_cliente) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista_cliente):
            print(i, valor)
    else:
        print('Escolha i, a ou l')
    

    





