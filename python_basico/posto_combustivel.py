gasolina = 0
alcool = 0
diesel = 0

while True:
    print("\n1. Abastecer com gasolina")
    print("2. Abastecer com alcool")
    print("3. Abastecer com diesel")
    print("4. Sair")

    opcao = input("Escolha sua opção: ")

    match opcao:
        case "1":
            gasolina += 1
            print("Abastecido com gasolina!")
        case "2":
            alcool += 1
            print("Abastecido com alcool")
        case "3":
            diesel += 1
            print("Abastecido com diesel")
        case "4":
            total_gasolina = gasolina
            total_alcool = alcool
            total_diesel = diesel
            print("\nAbastecimentos com gasolina: ", total_gasolina)
            print("Abastecimentos com alcool: ", total_alcool)
            print("Abastecimentos com diesel: ", total_diesel)
            print("Muito obrigado!")
            break

