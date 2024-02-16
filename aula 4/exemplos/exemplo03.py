vetor1 = [1, 2, 3]
vetor2 = [4, 5, 6]

soma = [] # Vetor vazio que armazenará o resultado da soma
for i in range(len(vetor1)): # Iteração por cada elemento dos vetores 
    soma.append(vetor1[i] + vetor2[i]) # Soma dos vetores. O resultado é adicionado ao vetor vazio "soma" pela função append()
print(soma)  # Exibir resultado armazenado no vetor "soma"
