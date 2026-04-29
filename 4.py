print("Condicionais e Booleanos")

salário = float(input("Digite seu salário: R$"))
parcela = float(input("Digite o valor da parcela: R$"))

limite = salário * 0.30
aprovado = parcela <= limite

if aprovado:
    print("Empréstimo Aprovado!")
else:
    print("Empréstimo Negado!")