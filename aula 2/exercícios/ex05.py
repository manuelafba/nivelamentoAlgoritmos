# Solicita que o usuário insira o peso e a altura e armazena em suas respectivas variáveis
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

imc = peso / (altura ** 2) # Fórmula do IMC

print(f"Seu IMC é: {imc}")

# Verifica cada condição do IMC e imprime uma classificação de acordo com cada resultado
if imc < 18.5:
    print("Abaixo do peso.")
elif imc <= 24.9:
    print("Peso normal.")
elif imc <= 29.9:
    print("Sobrepeso.")
else:
    print("Obesidade.")
