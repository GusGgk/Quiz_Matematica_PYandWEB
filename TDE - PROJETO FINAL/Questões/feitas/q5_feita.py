"""ENUNCIADO
Calcule a raiz de índice par de um número.
Esse tipo de raiz só é possível se o número for positivo ou zero."""
def q5():
    print("-"*30)
    print("QUESTÃO 5 - Raiz de Índice Par com Número Negativo")
    print("-"*30)

    indice = int(input("Digite o índice da raiz: "))
    radicando = float(input("Digite o número para extrair a raiz: "))

    if indice % 2 != 0 or radicando >= 0:
        
        resultado = radicando ** (1 / indice)
        print(f"O resultado da raiz é: {resultado:.2f}")
    else:
        print("Não é possível extrair raiz de índice par de número negativo.")

if __name__ == "__main__":
    q5()
