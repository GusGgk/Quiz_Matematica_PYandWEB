"""ENUNCIADO
Calcule a raiz de índice par de um número.
Esse tipo de raiz só é possível se o número for positivo ou zero."""

indice = int(input("Digite o índice da raiz: "))
radicando = float(input("Digite o número para extrair a raiz: "))

if ___________:  # A) indice % 2 != 0 or radicando >= 0
                 # B) indice % 2 == 0 and radicando < 0
                 # C) radicando != 0
    resultado = radicando ** (1 / indice)
    print(f"O resultado da raiz é: {resultado:.2f}")
else:
    print("Não é possível extrair raiz de índice par de ___________.") #a) numero negativo, b) numero positivo c) numero neutro
