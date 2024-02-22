from random import randint

numeroAleatorio = randint(1, 20)
tentativas = 0

print("Bem-vindo ao jogo de adivinhação! Estou pensando em um número entre 1 e 20.")

palpite = 0
while palpite != numeroAleatorio:
    palpite = int(input("Tente adivinhar qual é o número: "))
    tentativas += 1

    if palpite < numeroAleatorio:
        print("O número que estou pensando é maior.")
    elif palpite > numeroAleatorio:
        print("O número que estou pensando é menor.")

print(f"Parabéns! Você acertou o número {numeroAleatorio} em {tentativas} tentativas.")

