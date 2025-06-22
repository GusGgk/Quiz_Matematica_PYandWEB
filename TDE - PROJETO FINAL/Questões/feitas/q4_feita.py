"""ENUNCIADO
Verifique se é possível realizar a divisão 1 / (x - 2).
Essa expressão não pode ser calculada quando x = 2, pois o denominador se anula e a divisão se torna inválida."""
def q4():
    print("-"*30)
    print("QUESTÃO 4 - DENOMINADOR COM EXPRESSÃO ALGÉBRICA")
    print("-"*30)

    num_user = float(input("Digite um número para calcular 1 / (x - 2): "))

    if num_user - 2 != 0 or num_user != 2:
        resultado = 1 / (num_user - 2)
        print(f"O resultado da expressão é: {resultado:.2f}")

    else:
        print("Não é possível dividir por zero. O valor de x não pode ser o mesmo de 2")

if __name__ == "__main__":
    q4()  