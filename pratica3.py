
precos = {
    1: 6.00,
    2: 6.50,
    3: 5.00,
    4: 3.00,
    5: 2.00
}


codigo = int(input("Digite o código do produto:"))
quantidade = int(input("Digite a quantidade do produto:"))


if codigo in precos:
    total = precos[codigo] * quantidade
    print(f"Total: R$ {total:.2f}")


