def q6():

    print("-" * 30)
    print("QUESTÃO 6 - POTÊNCIA COM BASE ZERO E EXPOENTE NEGATIVO")
    print("-" * 30)

    base = float(input("Digite a base da potência: "))
    expoente = float(input("Digite o expoente: "))

    if base != 0 or expoente >= 0:
        resultado = base ** expoente
        print(f"O resultado é: {resultado:.2f}")
    else:
        print("Não é possível elevar zero a um expoente negativo. Isso gera divisão por zero.")


if __name__ == "__main__":
    q6()