print("Variáveis e Operações Matemáticas")

soma = 0

for i in range(3):
    nota = float(input(f"Digite sua {i+1}º Nota: "))
    soma += nota

média = soma / 3

print(f"Sua média é igual a: {média:.2f}")
