def exibir_menu():
    print("---------------------")
    print("Verificador de Meses")
    print("---------------------")
    print("1 - Verificar mês")
    print("0 - Sair do programa")


def exibir_resultado(numero, mes):
    print(f"\nO número {numero} corresponde ao mês de {mes}.\n")


def verificar_mes():
    try:
        numero = int(input("Digite um número inteiro entre 1 e 12: "))

        if 1 <= numero <= 12:
            meses = [
                "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
                "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
            ]
            mes = meses[numero - 1]
            exibir_resultado(numero, mes)
        else:
            print("\nNúmero inválido. O número deve estar entre 1 e 12.\n")

    except ValueError:
        print("\nErro: Por favor, insira apenas números inteiros.\n")


def main():
    while True:
        exibir_menu()
        opcao = input("Opção: ")

        if opcao == "1":
            verificar_mes()
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.\n")


if __name__ == "__main__":
    main()
