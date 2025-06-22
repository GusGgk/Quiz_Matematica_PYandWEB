def q9():
    import math

    print("-" * 30)
    print("QUESTÃO 9 - BASE INVÁLIDA EM LOGARITMO")
    print("-" * 30)

    valor = float(input("Digite o valor para o logaritmo: "))
    base = float(input("Digite a base do logaritmo: "))

    if valor > 0 and base > 0 and base != 1:
        resultado = math.log(valor, base)
        print(f"O logaritmo de {valor} na base {base} é {resultado:.2f}")
    else:
        print("O valor e a base devem ser positivos, e a base diferente de 1.")

if __name__ == "__main__":
    q9()