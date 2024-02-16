notas = []
media = 0

for i in range(8):
    nota = int(input(f"Digite a nota do {i+1}º aluno: "))
    notas.append(nota)
    media = sum(notas) / 8

print(notas)
print(media)

