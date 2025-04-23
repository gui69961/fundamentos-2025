from random import randint

# Criando a matriz 10x15 com números inteiros aleatórios entre 0 e 100
M = [[randint(0, 100) for _ in range(15)] for _ in range(10)]

# Exibindo a matriz completa
print("Matriz completa:")
for linha in M:
    print(linha)

# Exibindo apenas os elementos da primeira coluna
print("\nElementos da primeira coluna:")
for linha in M:
    print(linha[0])
