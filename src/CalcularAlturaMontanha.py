import math


def calcular_altura_montanha(altitude_aviao, angulo_depressao, distancia_horizontal):
    # Converter o ângulo para radianos
    angulo_rad = math.radians(angulo_depressao)

    # Calcular a altura da montanha usando a tangente
    altura_montanha = math.tan(angulo_rad) * distancia_horizontal

    # Altura total da montanha
    altura_total = altitude_aviao + altura_montanha

    return altura_total


def main():
    while True:
        try:
            altitude_aviao = float(input("Digite a altitude do avião (em km): "))
            angulo_depressao = float(input("Digite o ângulo de depressão (em graus): "))
            distancia_horizontal = float(input("Digite a distância horizontal até a montanha (em km): "))

            altura_total = calcular_altura_montanha(altitude_aviao, angulo_depressao, distancia_horizontal)
            print(f"A altura total da montanha é aproximadamente {altura_total:.2f} km\n")

            continuar = input("Deseja calcular novamente? (s/n): ").strip().lower()
            if continuar != 's':
                break
        except ValueError:
            print("Por favor, insira valores numéricos válidos.\n")


if __name__ == "__main__":
    main()
