PI=3.1415


#recupera do usuario o raio e a altura do cilindro
raio= float(input("digite o raio do cilindro:"))
altura= float(input("digite a altura do cilindro"))
# calcular area lateral

area_base = PI * raio ** 2

# calcular a area lateral

area_lateral= altura * 2 * PI * raio

area_cilindro= area_base + area_lateral

print(f"area a ser pintada:{area_cilindro: .2f}")

#calcular o volume de tinta
volume_tinta= area_cilindro/ 3
print(f"qtde de litros necessarios:{volume_tinta: 2f}")

latas_tinta= (volume_tinta/ 5)
print(f"qtde de latas de tinta: {latas_tinta}")


preço_unitario=latas_tinta
if latas_tinta==1:preço_unitario=50
if latas_tinta==2:preço_unitario= 48
if latas_tinta==3:preço_unitario= 46
if latas_tinta==4:preço_unitario=44


print(f"preço unitario: {preço_unitario}")

print(f"custo total: {latas_tinta* preço_unitario: .2f}")