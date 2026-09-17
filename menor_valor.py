a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

valores=[a, b, c]

def menor_valor(valores):
    menor = valores[0]
    for valor in valores[1:]:
        if valor < menor:
            menor = valor

    return str(menor)


print("Menor valor: " + menor_valor(valores))