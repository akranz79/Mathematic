import math


def calcular_montante(capital, taxa, anos):
    taxa_decimal = taxa / 100
    montante = capital * (1 + taxa_decimal) ** anos
    return montante


def main():
    while True:
        try:
            capital = float(input("Digite o valor do investimento inicial (R$): "))
            taxa = float(input("Digite a taxa de juros anual (%): "))
            anos = int(input("Digite o período de investimento (anos): "))

            montante = calcular_montante(capital, taxa, anos)
            print(f"\nApós {anos} anos, João terá R$ {montante:.2f} na conta.\n")

            if input("Deseja calcular outro investimento? (s/n): ").strip().lower() != 's':
                break
        except ValueError:
            print("Por favor, insira valores numéricos válidos.\n")


if __name__ == "__main__":
    main()
