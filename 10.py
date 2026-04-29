print("Desafio Final: Tudo Junto")
print("=" * 50)
print("Simulador de Carrinho de Compras")
print("=" * 50)

precos = []

while True:
    nome_produto = input("\nDigite o nome do produto (ou 'sair' para finalizar): ").strip()

    if nome_produto.lower() == "sair":
        break
    
    try:
        preco = float(input(f"Digite o preço de '{nome_produto}': R$ "))
        
        if preco < 0:
            print("Erro: O preço não pode ser negativo. Tente novamente.")
            continue
        
        precos.append(preco)
        print(f"✓ Produto '{nome_produto}' adicionado ao carrinho (R$ {preco:.2f})")
        
    except ValueError:
        print("Erro: Preço inválido. Digite um número válido.")
        continue

total_original = sum(precos)

if total_original > 100:
    desconto = total_original * 0.10
    total_final = total_original - desconto
    print("\n" + "=" * 50)
    print("RESUMO DA COMPRA")
    print("=" * 50)
    print(f"Total original: R$ {total_original:.2f}")
    print(f"Desconto (10%): R$ {desconto:.2f}")
    print(f"TOTAL A PAGAR: R$ {total_final:.2f}")
else:
    total_final = total_original
    print("\n" + "=" * 50)
    print("RESUMO DA COMPRA")
    print("=" * 50)
    print(f"TOTAL A PAGAR: R$ {total_final:.2f}")

print("=" * 50)

