print("Estruturas de Repetição")

usuário = input("Digite seu usuário: ")
print(f"Olá {usuário}, Seja bem-vindo")

senha = input("Digite a senha: ")

while senha != "python123":
    print("Senha incorreta")
    senha = input("Digite novamente: ")

print("Acesso concedido")