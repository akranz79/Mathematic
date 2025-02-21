import math


def calcular_montante(capital, taxa, anos, aporte_mensal=0):
    taxa_decimal = taxa / 100
    montante = capital
    for _ in range(anos * 12):  # Simulação mês a mês
        montante = (montante + aporte_mensal) * (1 + taxa_decimal / 12)
    return montante


def calcular_investimento_para_objetivo(taxa, anos, montante_desejado, aporte_mensal=0):
    taxa_decimal = taxa / 100
    montante = 0
    capital_inicial = 0

    for _ in range(anos * 12):  # Simulação mês a mês
        montante = (montante + aporte_mensal) * (1 + taxa_decimal / 12)

    # Recalculando o capital inicial necessário
    capital_inicial = montante_desejado / (1 + taxa_decimal / 12) ** (anos * 12)
    return capital_inicial, aporte_mensal


def main():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Calcular o montante final com aporte mensal")
        print("2 - Calcular o investimento inicial e aportes para atingir uma quantia específica")
        print("3 - Sair")

        opcao = input("Digite a opção desejada: ").strip()

        if opcao == "1":
            try:
                capital = float(input("Digite o valor do investimento inicial (R$): "))
                taxa = float(input("Digite a taxa de juros anual (%): "))
                anos = int(input("Digite o período de investimento (anos): "))
                aporte_mensal = float(input("Digite o valor do aporte mensal (R$): "))

                montante = calcular_montante(capital, taxa, anos, aporte_mensal)
                print(
                    f"\nApós {anos} anos, com aportes mensais de R$ {aporte_mensal:.2f}, você terá R$ {montante:.2f} na conta.\n")

            except ValueError:
                print("Por favor, insira valores numéricos válidos.\n")

        elif opcao == "2":
            try:
                taxa = float(input("Digite a taxa de juros anual (%): "))
                anos = int(input("Digite o período de investimento (anos): "))
                montante_desejado = float(input("Digite o valor desejado (R$): "))
                aporte_mensal = float(input("Digite o valor do aporte mensal (R$): "))

                capital_inicial, aporte_mensal = calcular_investimento_para_objetivo(taxa, anos, montante_desejado,
                                                                                     aporte_mensal)
                print(
                    f"\nPara atingir R$ {montante_desejado:.2f} após {anos} anos com aportes mensais de R$ {aporte_mensal:.2f}, o capital inicial necessário seria R$ {capital_inicial:.2f}.\n")

            except ValueError:
                print("Por favor, insira valores numéricos válidos.\n")

        elif opcao == "3":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida, tente novamente.\n")


if __name__ == "__main__":
    main()
