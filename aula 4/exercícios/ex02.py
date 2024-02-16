vetorPar = []
vetorImpar = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    if numero % 2 == 0:
        vetorPar.append(numero)
    else:
        vetorImpar.append(numero)

print(vetorPar)
print(vetorImpar)