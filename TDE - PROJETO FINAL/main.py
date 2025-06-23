import os
import webbrowser
from Questões.feitas.q1_feita import q1
from Questões.feitas.q2_feita import q2
from Questões.feitas.q3_feita import q3
from Questões.feitas.q4_feita import q4
from Questões.feitas.q5_feita import q5
from Questões.feitas.q6_feita import q6
from Questões.feitas.q7_feita import q7
from Questões.feitas.q8_feita import q8
from Questões.feitas.q9_feita import q9
from Questões.feitas.q10_feita import q10


def abrir_interface_web():
    print("Abrindo o quiz no navegador...")
    webbrowser.open("http://127.0.0.1:5500/TDE%20-%20PROJETO%20FINAL/FrontEnd/index.html")

def menu_python():
    print("\nQUESTÕES RESOLVIDAS EM PYTHON")
    print("(simulação do backend funcional)")
    print("1. Divisão por Zero")
    print("2. Raiz Quadrada de Número Negativo")
    print("3. Logaritmo de Número Não Positivo")
    print("4. Denominador com Expressão Algébrica")
    print("5. Raiz de Índice Par de Número Negativo")
    print("6. Potência com Base Zero e Expoente Negativo")
    print("7. Módulo com Divisor Zero")
    print("8. Expressão Quadrática no Denominador")
    print("9. Base Inválida em Logaritmo")
    print("10. Raiz Cúbica de Número Negativo")
    print("0. Sair")

    funcoes = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

    while True:
        opcao = input("\nEscolha uma questão (1 a 10) (0 fecha): ")
        if opcao == "0":
            break
        elif opcao.isdigit() and 1 <= int(opcao) <= 10:
            try:
                funcoes[int(opcao) - 1]()
            except Exception as e:
                print("Erro ao executar a questão:", e)
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    print("\nProjeto: Quiz de Restrições Matemáticas em Python")
    print("1. Abrir interface web")
    print("2. Executar versão Python (terminal)")
    escolha = input("Escolha uma opção (1 ou 2): ")

    if escolha == "1":
        abrir_interface_web()
    elif escolha == "2":
        menu_python()
    else:
        print("Opção inválida.")
