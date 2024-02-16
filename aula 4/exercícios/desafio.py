matriz = []

print("Digite os elementos da matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        elemento = int(input(f"Digite o elemento da posição [{i}][{j}]: "))
        linha.append(elemento)
    matriz.append(linha)

soma = 0
for linha in matriz:
    soma += sum(linha)

print(f"A soma de todos os elementos da matriz é: {soma}")
