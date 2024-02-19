a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

auxiliar = a # O valor de A é guardado na variável auxiliar
a = b # O valor de B é armazenado na variável A
b = auxiliar # A variável B recebe o valor das variável auxiliar, que é o valor incial de A

print(a)
print(b)
