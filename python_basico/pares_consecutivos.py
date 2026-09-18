def get_soma_pares(num, quantidade=5):
    soma = 0

    if num % 2 != 0:
        num += 1

    for _ in range(quantidade):
        soma += num
        num +=2

    return soma

while True:
    numero = int(input("Digite um número inteiro: "))
    if numero == 0:
        break

    soma = get_soma_pares(numero)
    print("Soma dos pares: ", soma)

