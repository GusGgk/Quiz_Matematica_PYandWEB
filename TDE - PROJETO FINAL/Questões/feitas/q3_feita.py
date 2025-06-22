"""ENUNCIADO
Verifique se é possível calcular o logaritmo de um número x.
No conjunto dos números reais, não é possível calcular o logaritmo de zero ou de números negativos."""
import math

def q3():
    print("-"*30)
    print("QUESTÃO 3 - LOGARITMO DE NÚMERO NÃO POSITIVO")
    print("-"*30)

    num_user = float(input("Digite um número para calcular o logaritmo: "))

    if num_user > 0:
        resultado = math.log(num_user)
        print(f"O logaritmo de {num_user} é {resultado:.2f}")
        
    else:
        print("Não é possível calcular o logaritmo de negativos ou 0 ,pois o domínio da função logarítmica exige números positivos.")
     
if __name__ == "__main__":
    q3()