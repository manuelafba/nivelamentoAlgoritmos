numero = int(input("Digite um número para a tabuada: "))

multiplicador = 0

print(f"=== Tabuada do {numero} ===")
while multiplicador < 10:
    multiplicador += 1
    print(f"{numero} x {multiplicador} = {numero * multiplicador}")
