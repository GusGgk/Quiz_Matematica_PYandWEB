"""ENUNCIADO
Verifique se é possível calcular o logaritmo de um número x.
No conjunto dos números reais, não é possível calcular o logaritmo de zero ou de números negativos."""
import math

print("-"*30)
print("QUESTÃO 3 - LOGARITMO DE NÚMERO NÃO POSITIVO")
print("-"*30)

# Substitua os espaços abaixo com a condição correta e a explicação matemática adequada

num_user = float(input("Digite um número para calcular o logaritmo: "))

if ___________: # A) num_user < 0   B) num_user > 0   C) num_user >= 0
    
    resultado = math.log(num_user)
    print(f"O logaritmo de {num_user} é {resultado:.2f}")
else: # A) negativos ou zero   B) pares   C) múltiplos de 10
    print("Não é possível calcular o logaritmo de ____________,pois o domínio da função logarítmica exige números positivos.")
    
