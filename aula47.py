"""
Faça um jogo para o usuário adivinhar qual 
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu 
usuário.
"""

import os

palavra_secreta = 'queijo'
letras_acertadas = ''
tentativas = 0

while True:
    letra_usuario = input('Descubra a palavra secreta, digite apenas uma letra: ')
    
    if len(letra_usuario)  > 1:
        print('Digite apenas uma letra')
        continue

    if letra_usuario in palavra_secreta:
        letras_acertadas += letra_usuario

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print('Palavra formada: ', palavra_formada)
    tentativas += 1

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('PARABÉNS, VOCÊ GANHOU!')
        print(f'A palavra era({tentativas}X)', palavra_secreta)
        letras_acertadas = ''
        tentativas = 0






