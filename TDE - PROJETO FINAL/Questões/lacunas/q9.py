import math

print("-" * 30)
print("QUESTÃO 9 - BASE INVÁLIDA EM LOGARITMO")
print("-" * 30)

valor = float(input("Digite o valor para o logaritmo: "))
base = float(input("Digite a base do logaritmo: "))

# Complete:
if ____:  # A) valor > 0 and base > 0 and base != 1   B) valor >= 0 and base != 0   C) valor < 0 and base < 0
    resultado = math.log(valor, base)
    print(f"O logaritmo de {valor} na base {base} é {resultado:.2f}")
else:
    print("A base deve ser positiva e diferente de ___________.")  # A) 1   B) 0   C) 10
