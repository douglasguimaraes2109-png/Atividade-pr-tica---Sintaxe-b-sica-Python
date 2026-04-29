print("Tipos de Dados e Strings")

nome = str(input("Digite seu Nome: "))
idade = int(input("Digite sua Idade: "))
altura = float(input("Digite sua Altura: "))

print(type(nome))
print(type(idade))
print(type(altura))

print((f"Olá, {nome}! Você tem {idade} anos e {altura}m de altura."))