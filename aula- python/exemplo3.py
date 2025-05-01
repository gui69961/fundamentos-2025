a=int(input("lado a: "))
b=int(input("lado b: "))
c=int(input("lado c: "))

if a + b + c and  b < a + c  and c < a + b: 
    if a==b and a==c and b == c: print( "triangulo equilatero")
    elif a== b or a==c or b==c: print("Triangulo isosceles")
    else: print("Trinagulo escaleno")
else: print("os lados nao formam um triangulo")