lista = []
soma = 0

quantidade_numeros = int(input("Quantos números deseja digitar? "))

for i in range(quantidade_numeros):
    numeros = float(input("Digite um número: "))
    lista.append(numeros)

for i in lista:
    soma += i
    media = soma/quantidade_numeros

print(f"Valores: {lista}")
print(f"Soma dos valores: {soma}")
print(f"Media dos valores: {media}")