dia_semana = input("Digite o nome de um dia da semana: ").lower()

if dia_semana == "sábado" or dia_semana == "domingo":
    print("Fim de semana")
elif dia_semana == "segunda" or dia_semana == "terça" or dia_semana == "quarta" or dia_semana == "quinta" or dia_semana == "sexta":
    print("Dia útil")
else:
    print("Entrada inválida. Por favor, insira um dia da semana válido.")
