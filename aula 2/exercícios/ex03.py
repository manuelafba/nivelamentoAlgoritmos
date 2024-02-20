numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0: # Se o número for divisível por 2
    print("Fizz")
elif numero % 5 == 0: # Se o número for divisível por 5
    print("Buzz")
else: # Se o número não for divisível por 2 nem 5
    print("Fizzbuzz")