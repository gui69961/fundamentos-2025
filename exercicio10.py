from random import randint, random

# Criando a lista de inteiros com 10 números aleatórios
lista_inteiros = [randint(0, 10) for _ in range(10)]

# Criando a lista de reais com 5 números aleatórios
lista_reais = [random() * 10 for _ in range(5)]

# Criando a lista de strings com 7 strings definidas por mim
lista_strings = ["banana", "sol", "teclado", "nuvem", "gato", "livro", "caneca"]

# Criando a lista completa com todas as outras listas dentro
completa = [lista_inteiros, lista_reais, lista_strings]

# Apagando as listas originais
del lista_inteiros
del lista_reais
del lista_strings

# Acessando e mostrando todos os elementos da lista completa
for sublista in completa:
    for elemento in sublista:
        print(elemento)
