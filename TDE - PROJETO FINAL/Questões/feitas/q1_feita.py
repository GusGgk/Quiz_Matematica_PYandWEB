"""ENUNCIADO
Verifique se é possível realizar a operação de divisão de 10 por um número qualquer x.
Lembre-se de que não é possível dividir nenhum número por zero."""
def q1():
    print("-"*30)
    print("QUESTÃO 1 - DIVISÃO POR 0")
    print("-"*30)

    numero_principal = 10
    num_user = float(input("Digite qualquer número para dividir por 10: "))

    if num_user != 0:
        resultado = numero_principal / num_user
        print(f"A divisão do {numero_principal} com o {num_user} é de {resultado:.2f}")
    else:    
        print("O denominador não pode ser 0... Divisões por 0 não são Permitidas Tente Novamente.")

if __name__ == "__main__":
    q1()