print("Repetição e Operações Matemáticas")

numero = int(input("Digite um número para ver a tabuada do mesmo: "))

for i in range(10):
    print(f"{numero} * {i+1}: {numero * (i+1)}")