from random import randint
vetor1 = []
vetor2 = []
vetorSoma = []

for i in range(10):
    vetor1.append(randint(1, 10))
    vetor2.append(randint(1, 10))

for i in range(10):
    soma = vetor1[i] + vetor2[i]
    vetorSoma.append(soma)

print(vetor1)
print(vetor2)
print(vetorSoma)

