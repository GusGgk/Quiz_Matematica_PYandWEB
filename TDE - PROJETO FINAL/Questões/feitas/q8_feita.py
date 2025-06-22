def q8():
    print("-" * 30)
    print("QUESTÃO 8 - EXPRESSÃO QUADRÁTICA NO DENOMINADOR")
    print("-" * 30)

    x = float(input("Digite um valor para x: "))

    if x != 2 and x != -2:
        resultado = 1 / (x ** 2 - 4)
        print(f"O resultado da expressão é: {resultado:.2f}")
    else:
        print("O valor de x não pode ser 2 ou -2, pois zera o denominador.")

if __name__ == "__main__":
    q8()