texto = input("Digite uma string:")

texto_convertido= ""

for letra in texto:
    if letra in "aeiou":
        texto_convertido = texto_convertido + chr(ord(letra)- 32)
    else:
        texto_convertido = texto_convertido + letra

        print("texto convertido :", texto_convertido)


