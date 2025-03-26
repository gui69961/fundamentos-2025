sexo= input("digite o seu sexo: ")
altura= float(input("digite a sua altura: ")) 
peso_ideal = (72.7 * altura) - 58
peso_idealf= (62.1 * altura) - 44,7


if sexo == "homem": print(f"peso ideal:{peso_ideal: .2f}")

if sexo == "mulher" : print (f"peso idealf: {peso_idealf: .2f}")

