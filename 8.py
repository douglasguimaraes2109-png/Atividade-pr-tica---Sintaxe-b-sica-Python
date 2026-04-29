print("Listas e Estruturas de Repetição")

numeros = []

print("Escolha 5 números para entrar na lista")
for i in range(5):
    num = int(input(f"Digite o {i+1}° número: "))
    numeros.append(num)

maior_numero = numeros[0]

for n in numeros:
    if n > maior_numero:
        maior_numero = n

print(f"A lista completa é: {numeros}")
print(f"O maior número inserido foi: {maior_numero}")