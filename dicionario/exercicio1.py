def procurarchave(dicionario,valor):
    chaves = []
    for chave, val in dicionario.items():
        if val == valor:
            chaves.append(chave)
            return chaves
        
        dicionario= {
            'alpha': 1,
            'bravo': 2,
            'charlie': 1,
            'delta': 3,
            'echo': 1
        }
print(procurarchave(dicionario, 1))
print(procurarchave(dicionario, 2))
print(procurarchave(dicionario, 3))
print(procurarchave(dicionario, 4))
print(procurarchave(dicionario, 5))