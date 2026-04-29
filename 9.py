print("Listas, Condicionais e Repetição")

numeros = [12, 5, 8, 12, 14, 33, 7]

pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)

print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")