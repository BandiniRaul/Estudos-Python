numero_informado = int (input("Quantos números deseja digitar? "))

for i in range(numero_informado):
    numeros = int(input("Digite um número: "))
    if numeros %2 == 0 and numeros > 0:
        print("Par positivo")
    elif numeros == 0:
        print("NULO")
    elif numeros %2 == 0 and numeros < 0:
        print("Par negativo")
    elif numeros %2 != 0 and numeros > 0:
        print("Ímpar positivo")
    else:
        print("Ímpar negativo")