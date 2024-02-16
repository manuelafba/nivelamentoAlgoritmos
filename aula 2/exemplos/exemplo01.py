a = 5
b = 10

# Operador AND
x = a > 0 and b > 0 # Verdadeiro, pois ambos são maiores que zero
print(x)

# Operador OR
y = a > 0 or b < 0 # Verdadeiro, pois pelo menos um dos números é maior que zero
print(y)

# Operador NOT
z = not x == 0 # A afirmação "x == 0" é falsa, pois x é diferente de zero. Porém, o operador NOT inverte o seu valor lógico, retornando TRUE 
print(z)