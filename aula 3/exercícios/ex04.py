qtdNegativos = 0
somaPositivos = 0

for i in range(1, 21):
    numero = int(input(f"Insira o {i}º número: "))
    if numero > 0:
        somaPositivos += numero
    else:
        qtdNegativos += 1

print(f"Quantidade de números negativos: {qtdNegativos}")
print(f"Soma dos números positivos: {somaPositivos}")

