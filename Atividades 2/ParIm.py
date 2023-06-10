while True:
    try:
        numero = int(input("Digite um número inteiro (ou '0' para sair): "))
        
        if numero == 0:
            print("Programa encerrado.")
            break
        
        if numero % 2 == 0:
            print(f"\nO número {numero} é par.\n")
        else:
            print(f"\nO número {numero} é ímpar.\n")
    
    except ValueError:
        print("Erro: Por favor, insira apenas números inteiros.\n")
