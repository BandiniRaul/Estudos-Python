while True:
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    if x == y:
        break
    if x < y:
        print("Crescente!")
    else:
        print("Decrescente!")