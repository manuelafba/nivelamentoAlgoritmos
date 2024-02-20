a = int(input("Insira o valor de A: "))
b = int(input("Insira o valor de B: "))
c = int(input("Insira o valor de C: "))

if a + b > c and a + c > b and b + c > a: # Condição para formar um triângulo
    print("Os lados formam um triângulo")
    if a == b == c: # Condição para ser um triângulo equilátero
        print("Triângulo equilátero")
    elif a == b or a == c or b == c: # Condição para ser um triângulo isósceles
        print("Triângulo isósceles")
    else: # Caso não obedeça nenhuma das condições, então ele é escaleno
        print("Triângulo escaleno")
else: # Caso a condição de existência do triângulo não for cumprida
    print("Os lados não formam um triângulo")