VALOR = 50.0

minutos = int(input("Digite quantos minutos foram usados: "))

if minutos > 100:
    excedentes = float(minutos-100)
    valorFinal = VALOR + (excedentes*2)
    print("Valor total a ser pago: R$" + str(f"{valorFinal: .2f}"))
else:
    print("Valor final a ser pago: R$" + str(f"{VALOR: .2f}"))

