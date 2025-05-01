import random

def roll_dice():
  die1 = random.randint(1, 6)
  die2 = random.randint(1, 6)
  return die1 + die2

def main():
  
  num_lancamentos = 1000
  frequencia_somas = {}


  for soma_possivel in range(2, 13):
    frequencia_somas[soma_possivel] = 0


  for _ in range(num_lancamentos):
    soma = roll_dice()
    frequencia_somas[soma] += 1

  print("Resultados da Simulação de 1000 Lançamentos de Dois Dados:")
  print("-" * 40)
  print(f"{'Soma':<8}{'Contagem':<12}{'Frequência (%)':<20}")
  print("-" * 40)

  for soma in sorted(frequencia_somas.keys()):
    contagem = frequencia_somas[soma]
    frequencia_percentual = (contagem / num_lancamentos) * 100
    print(f"{soma:<8}{contagem:<12}{frequencia_percentual:<20.2f}")

  print("-" * 40)


if __name__ == "__main__":
  main()
