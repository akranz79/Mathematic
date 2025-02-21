import math


def calcular_cateto_oposto(hipotenusa, angulo):
    # Converter o ângulo para radianos
    angulo_rad = math.radians(angulo)

    # Calcular o cateto oposto usando o seno
    cateto_oposto = math.sin(angulo_rad) * hipotenusa

    return cateto_oposto


def main():
    while True:
        try:
            hipotenusa = float(input("Digite o comprimento da hipotenusa (em cm): "))
            angulo = float(input("Digite o ângulo (em graus): "))

            cateto_oposto = calcular_cateto_oposto(hipotenusa, angulo)
            print(f"O comprimento do cateto oposto é aproximadamente {cateto_oposto:.2f} cm\n")

            continuar = input("Deseja calcular novamente? (s/n): ").strip().lower()
            if continuar != 's':
                break
        except ValueError:
            print("Por favor, insira valores numéricos válidos.\n")


if __name__ == "__main__":
    main()
