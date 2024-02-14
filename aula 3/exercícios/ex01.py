numero = int(input("Escolha um número para a tabuada:\n"))

# Usando loop FOR
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Usando loop WHILE
j = 1

while j <= 10:
    print(f"{numero} x {j} = {numero * j}")
    j += 1