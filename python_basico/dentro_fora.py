dentro = 0
fora = 0

numero_informado = int(input("Quantos números deseja digitar? "))

for i in range(numero_informado):
    numeros = int(input("Digite um número: "))
    if numeros >= 10 and numeros <= 20:
        dentro += 1
    else:
        fora += 1

print("Números dentro: ", dentro)
print("Números fora: ", fora)