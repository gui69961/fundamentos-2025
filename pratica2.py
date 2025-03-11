from math import sqrt



forma = input("Você deseja calcular o volume do dodecaedro ou icosaedro: ").lower()
valor = float(input("Digite o valor da aresta a em metros: "))


if forma == "dodecaedro":
    volume_dodecaedro = (15 + 7 * sqrt(5)) / 4 * valor ** 3
    print(f"O volume de um dodecaedro regular com {valor: .2f} de aresta  é: {volume_dodecaedro:.2f}.")

elif forma == "icosaedro":
    volume_icosaedro = (5/12 * (3+ sqrt(5)) * valor ** 3)
    print(f"O volume de um icosaedro regular com  {valor: .2f} de aresta  é: {volume_icosaedro:.2f}.")
