"""ENUNCIADO
Verifique se é possível realizar a divisão 1 / (x - 2).
Essa expressão não pode ser calculada quando x = 2, pois o denominador se anula e a divisão se torna inválida."""

print("-"*30)
print("QUESTÃO 4 - DENOMINADOR COM EXPRESSÃO ALGÉBRICA")
print("-"*30)

num_user = float(input("Digite um número para calcular 1 / (x - 2): "))

if _______:  # A) num_user != 2  B) num_user > 0   C) num_user == 2
    resultado = 1 / (num_user - 2)
    print(f"O resultado da expressão é: {resultado:.2f}")

else:
    print("Não é possível dividir por zero. O valor informado não pode ser ______") #A) 2 para não zerar B) 0 para não virar 1 C) 5 para não dar numero quebrado
    

    