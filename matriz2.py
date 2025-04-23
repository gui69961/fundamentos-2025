# Criando uma matriz 3x3 a partir da entrada do usuário
matriz = []

print("Digite os elementos da matriz 3x3:")

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Exibindo a matriz
print("\nMatriz informada:")
for linha in matriz:
    print(linha)

# Calculando a soma da diagonal principal
soma_diagonal = sum(matriz[i][i] for i in range(3))

print(f"\nSoma da diagonal principal: {soma_diagonal}")
