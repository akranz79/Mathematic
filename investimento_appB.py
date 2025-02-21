def calcular_montante(C, A, T, J):
    montante = C * ((1 + J/100) ** (T / 12))
    for i in range(1, int(T) + 1):
        montante += A * ((1 + J/100) ** ((T - i) / 12))
    return montante

def calcular_capital(M, A, T, J):
    montante = M
    for i in range(1, int(T) + 1):
        montante -= A * ((1 + J/100) ** ((T - i) / 12))
    capital = montante / ((1 + J/100) ** (T / 12))
    return capital

def calcular_aporte(C, M, T, J):
    montante = M - C * ((1 + J/100) ** (T / 12))
    aporte = montante / sum([(1 + J/100) ** ((T - i) / 12) for i in range(1, int(T) + 1)])
    return aporte

def calcular_tempo(C, A, M, J):
    tempo = 0
    montante = C
    while montante < M:
        montante += A
        montante *= (1 + J/100) ** (1 / 12)
        tempo += 1
    return tempo

def encontrar_opcao_equilibrada(S, T, J):
    melhor_C, melhor_A = 0, 0
    menor_diferenca = float('inf')
    for C in range(1, int(S) + 1):
        for A in range(1, int(S) + 1 - C):
            montante = calcular_montante(C, A, T, J)
            diferenca = abs(S - (C + A))
            if diferenca < menor_diferenca:
                menor_diferenca = diferenca
                melhor_C, melhor_A = C, A
    return melhor_C, melhor_A

def formatar_valor(valor):
    return "{:,.2f}".format(valor).replace(",", "X").replace(".", ",").replace("X", "")

def menu():
    while True:
        print("\nMenu de Opções:")
        print("a. Calcular Montante (M)")
        print("b. Calcular Capital Inicial (C)")
        print("c. Calcular Aporte Mensal (A)")
        print("d. Calcular Tempo de Investimento (T)")
        print("e. Encontrar Opção Mais Equilibrada")
        print("f. Finalizar Programa")

        opcao = input("Escolha uma opção: ").lower()

        if opcao == 'a':
            C = float(input("Capital inicial (C): "))
            A = float(input("Aporte mensal (A): "))
            T = float(input("Tempo de investimento em meses (T): "))
            J = float(input("Juros anuais (%) (J): "))
            M = calcular_montante(C, A, T, J)
            print(f"Montante após {T} meses: {formatar_valor(M)}")

        elif opcao == 'b':
            M = float(input("Montante desejado (M): "))
            A = float(input("Aporte mensal (A): "))
            T = float(input("Tempo de investimento em meses (T): "))
            J = float(input("Juros anuais (%) (J): "))
            C = calcular_capital(M, A, T, J)
            print(f"Capital inicial necessário (C): {formatar_valor(C)}")

        elif opcao == 'c':
            C = float(input("Capital inicial (C): "))
            M = float(input("Montante desejado (M): "))
            T = float(input("Tempo de investimento em meses (T): "))
            J = float(input("Juros anuais (%) (J): "))
            A = calcular_aporte(C, M, T, J)
            print(f"Aporte mensal necessário (A): {formatar_valor(A)}")

        elif opcao == 'd':
            C = float(input("Capital inicial (C): "))
            A = float(input("Aporte mensal (A): "))
            M = float(input("Montante desejado (M): "))
            J = float(input("Juros anuais (%) (J): "))
            T = calcular_tempo(C, A, M, J)
            print(f"Tempo necessário para alcançar o montante (T): {formatar_valor(T)} meses")

        elif opcao == 'e':
            S = float(input("Salário (S): "))
            T = float(input("Tempo de investimento em meses (T): "))
            J = float(input("Juros anuais (%) (J): "))
            melhor_C, melhor_A = encontrar_opcao_equilibrada(S, T, J)
            print(f"Opção mais equilibrada - Capital inicial (C): {formatar_valor(melhor_C)}, Aporte mensal (A): {formatar_valor(melhor_A)}")

        elif opcao == 'f':
            print("Programa finalizado.")
            break

        else:
            print("Opção inválida!")

# Executa o menu
menu()
