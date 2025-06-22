"""ENUNCIADO
Verifique se é possível calcular a raiz quadrada de um número.
Lembre-se de que não é possível calcular a raiz quadrada de números negativos dentro do conjunto dos números reais.
"""
def q2():
    import math

    print("-"*30)
    print("QUESTÃO 2 - RAIZ QUADRADA DE NÚMERO NEGATIVO")
    print("-"*30)

    num_user = float(input("Digite um número para calcular a raíz Quadrada: "))

    if num_user >= 0:
        resultado = math.sqrt(num_user)
        print(f"A raiz quadrada de {num_user} é de {resultado}")
    else:
        print("Não é possível calcular a raiz quadrada de números menores que 0, no conjunto de números reais.")
    
if __name__ == "__main__":
    q2()