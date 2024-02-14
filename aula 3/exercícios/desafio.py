from random import randint

numeroAleatorio = randint(1, 20)
tentativas = 0


while True:
    palpite = int(input("Tente adivinhar o número entre 1 e 20: "))
    tentativas += 1

    if palpite == numeroAleatorio:
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas")
        break
    elif palpite > numeroAleatorio:
        print(f"O número aleatório é menor que {palpite}")
    else:
        print(f"O número aleatório é maior que {palpite}")
