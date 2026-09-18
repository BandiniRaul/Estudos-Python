soma_impar = 0

numero_x = int(input("Digite o primeiro número: "))
numero_y = int(input("\nDigite o segundo número: "))
menor = min(numero_x, numero_y)
maior = max(numero_x, numero_y)

numeros_entre = list(range(menor+1, maior))
for i in numeros_entre:
    if i %2 != 0:
        soma_impar += i

print("Soma dos valores ímpares: ",soma_impar)
