print("Estruturas Condicionais")

velocidade = int(input("Digite a velocidade: "))

if velocidade > 80:
    Km_ultrapassado = velocidade - 80
    multa = Km_ultrapassado * 5
    print(f"Alerta! Você ultrapassou a velocidade limite, Sua velocidade: {velocidade}Km/h \nSua multa é de {multa}R$")
else:
    print("Velocidade dentro do limite.")
