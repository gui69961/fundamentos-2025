with open("texto.txt", "r") as arquivo:
    conteudo= arquivo.read()
    conteudo.strip(".,;:?(){}<> / ""'")
    palavras = conteudo.split()
    print(palavras)

    palavras_limpas = []
    for palava in palavras: 
        palavra = palavra.strip(".,;:?(){}<> / ""'")
        palavras_limpas.append(palavra)
        
        comprimento_palavaras= []
        for palavra in palavras_limpas:
            comprimento_palavaras.append(len(palavra))
            print(f"{palavras_limpas}")
            print(f"{comprimento_palavaras}")

            maior_comprimento= max(comprimento_palavaras)
            palavras_maiores= []
            for palavra in palavras_limpas:
                if len(palavra) == maior_comprimento:
                    palavras_maiores.append(palavra)

                    print(f"A(s) palavra(s) mais longas tem {maior_comprimento} caracteres:")
                    print("as palavras sao:")
                    for palavra in palavras_maiores:
                        print(palavra)