
h_inicial = int(input("Digite a hora inicial: "))
m_inicial = int(input("Digite o minuto inicial:"))
h_final = int(input("Digite a hora final: "))
m_final = int(input("Digite o minuto final: "))


inicio_total = h_inicial * 60 + m_inicial
final_total = h_final * 60 + m_final


if final_total <= inicio_total:
    duracao_total = (24 * 60 - inicio_total) + final_total
else:
    duracao_total = final_total - inicio_total


horas = duracao_total // 60
minutos = duracao_total % 60

print(f"O jogo durou {horas} hora(s) e {minutos} minutos(s)")


