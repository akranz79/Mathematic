
def exibir_tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def main():
    numero = int(input("Digite um numero inteiro: "))
    exibir_tabuada(numero)


if __name__== "__main__":
    main()




