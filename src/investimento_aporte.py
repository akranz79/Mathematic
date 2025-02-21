import math


def calcular_montante(capital, taxa, anos, aporte_mensal=0):
    taxa_decimal = taxa / 100
    montante = capital
    for _ in range(anos * 12):  # Simulação mês a mês
        montante = (montante + aporte_mensal) * (1 + taxa_decimal / 12)
    return montante


def main():
    while True:
        try:
            capital = float(input("Digite o valor do investimento inicial (R$): "))
            taxa = float(input("Digite a taxa de juros anual (%): "))
            anos = int(input("Digite o período de investimento (anos): "))
            aporte_mensal = float(input("Digite o valor do aporte mensal (R$): "))

            montante = calcular_montante(capital, taxa, anos, aporte_mensal)
            print(
                f"\nApós {anos} anos, com aportes mensais de R$ {aporte_mensal:.2f}, João terá R$ {montante:.2f} na conta.\n")

            if input("Deseja calcular outro investimento? (s/n): ").strip().lower() != 's':
                break
        except ValueError:
            print("Por favor, insira valores numéricos válidos.\n")


if __name__ == "__main__":
    main()
