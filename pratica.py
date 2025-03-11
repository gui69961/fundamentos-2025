primeiro = int(input("Digite o valor do primeiro produto: "))
segundo = int(input("Digite o valor do segundo produto: "))
terceiro = int(input("Digite o valor do terceiro produto: "))  

Preço = primeiro + segundo + terceiro
Desconto = Preço * 0.10
Desconto_maior = Preço * 0.20

if Preço < 500:
    print(f"Desconto: {Desconto:.2f}")  
else:
    print(f"Desconto: {Desconto_maior:.2f}") 

