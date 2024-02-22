somaPositivos = 0
qtdNegativos = 0

for i in range(0, 10):
    numero = int(input("Digite o valor"))
    if numero > 0:
        somaPositivos += numero
    else:  
        qtdNegativos += 1

print(f'Soma dos positivos = {somaPositivos}')
print(f'Negativos = {qtdNegativos}')