import random


def lancar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2


def simular_lancamentos(qtd_lancamentos=1000):
    frequencias = {}

    for soma in range(2, 13):
        frequencias[soma] = 0

   
    for _ in range(qtd_lancamentos):
        resultado = lancar_dados()
        frequencias[resultado] += 1

   
    print("Resultado | Frequência (%)")
    print("--------------------------")
    for soma in range(2, 13):
        porcentagem = (frequencias[soma] / qtd_lancamentos) * 100
        print(f"{soma:^9} | {porcentagem:>10.2f}%")


simular_lancamentos()
