numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("Fizz")
elif numero % 5 == 0:
    print("Buzz")
else:
    print("Fizzbuzz")