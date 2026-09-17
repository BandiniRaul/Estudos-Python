def celcius_fahrenheit(celsius):
    return (celsius*1.8) + 32 

def fahrenheit_celcius(fahrenheit):
    return (fahrenheit - 32) * (5/9)


while True:
    tipo_temperatura = int(input("Escolha o tipo de temperatura que deseja consultar:\n1.Celsius\n2.Fahrenheit\n3.Sair\nEscolha: "))

    if tipo_temperatura == 3:
        print("Programa encerrado")
        break

    if tipo_temperatura == 1:
        temperatura = float(input("Digite a temperatura em Celsius: "))
        opcoes = int(input("\n1. Ver temperatura atual\n2. Converter para Fahrenheit\nEscolha: "))
        if opcoes == 1:
            print(f"Temperatura atual: {temperatura:.2f} °C")
        elif opcoes == 2:
            resultado = celcius_fahrenheit(temperatura)
            print(f"Temperatura em Fahrenheit: {resultado:.2f} °F")
        else:
            print("Digite uma opção válida!")

    elif tipo_temperatura == 2:
        temperatura = float(input("Digite a temperatura em Fahrenheit: "))
        opcoes = int(input("\n1. Ver temperatura atual\n2. Converter para Celsius\nEscolha: "))
        if opcoes == 1:
            print(f"Temperatura atual: {temperatura:.2f} °F")
        elif opcoes == 2:
            resultado = fahrenheit_celcius(temperatura)
            print(f"Temperatura em Celsius: {resultado:.2f} °C")
        else:
            print("Digite uma opção válida!")