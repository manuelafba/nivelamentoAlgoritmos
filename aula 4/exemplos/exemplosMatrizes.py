matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[1][2]) # Segundo elemento, terceira coluna

for linha in matriz: # Iteração sobre cada linha da matriz
    for elemento in linha: # Iteração sobre cada elemento da linha
        print(elemento, end=' ') # Printa o elemento com um espaço para separá-los
    print() # Quebra de linha
