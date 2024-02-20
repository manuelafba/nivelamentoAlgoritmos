nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Sua média é {media}")

if media >= 7: # Condição para ser aprovado: média maior ou igual a 7
    print("Aprovado!")
else: # Caso contrário, a mensagem "Reprovado" aparecerá
    print("Reprovado!")