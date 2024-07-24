# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro

# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 4

# print(duplicar(2))
# print(triplicar(2))
# print(quadruplicar(2))

def criar_multiplicacao(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = (criar_multiplicacao(2))
triplicar = (criar_multiplicacao(3)) 
quadruplicar = (criar_multiplicacao(4))

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))