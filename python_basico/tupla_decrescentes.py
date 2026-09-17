# TUPLA (), (X, Y)
# Receber infinitamenta até digitar -1
# Depois disso (-1), ele para cada tupla ele deve mostrar o X e o Y e falar se é decrescente ou crescente

lista_tuplas: list[tuple] = []

while True:
    print("\n1. Digitar a dupla de números ")
    print("2. Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            x = int(input("Digite o primeiro número: "))
            y = int(input("\nDigite o segundo número: "))
            tupla = (x, y)
            lista_tuplas.append(tupla)
            print("Tupla armazenada")

        case "2":
            for t in lista_tuplas:
                x, y = t # desempacotamento da tupla
                if x < y:
                    print("Ordem crescente")
                else:
                    print("Ordem decrescente")
            break