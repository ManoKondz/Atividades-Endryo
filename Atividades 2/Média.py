nota1 = 0
nota2 = 0

while True:
    try:
        nota1 = float(input("Digite a primeira nota: "))
        break
    except ValueError:
        print("Erro: Por favor, insira apenas valores numéricos para a primeira nota.")

while True:
    try:
        nota2 = float(input("Digite a segunda nota: "))
        break
    except ValueError:
        print("Erro: Por favor, insira apenas valores numéricos para a segunda nota.")

media = (nota1 + nota2) / 2

print("\n=== Resultado ===")
print(f"Nota 1: {nota1:.2f}")
print(f"Nota 2: {nota2:.2f}")
print(f"Média: {media:.2f}")

if media >= 7:
    print("Situação: Aprovado")
else:
    print("Situação: Reprovado")
