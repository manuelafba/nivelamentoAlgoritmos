soma = 0

numero = int(input("Digite um número inteiro positivo ou 0 para parar a entrada: "))

while numero != 0:
    soma += numero
    numero = int(input("Digite um número inteiro positivo ou 0 para parar a entrada: "))

print(f"A soma dos números inseridos é igual a {soma}")
