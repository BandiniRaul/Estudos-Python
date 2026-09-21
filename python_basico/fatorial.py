numero_informado = int(input("Digite um número inteiro para calcular o fatorial: "))
resultado = 1

for n in range(1, numero_informado+1):
    if numero_informado > 15:
        print("Digite um número inteiro menor que 15!")
        continue
    resultado *= n

print("Fatorial: ", resultado)
