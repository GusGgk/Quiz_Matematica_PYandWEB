def q10():
    print("-" * 30)
    print("QUESTÃO 10 - RAIZ CÚBICA DE NÚMERO NEGATIVO")
    print("-" * 30)

    num = float(input("Digite um número: "))

    resultado = num ** (1/3)
    print(f"A raiz cúbica de {num} é aproximadamente {resultado:.2f}")

if __name__ == "__main__":
    q10()