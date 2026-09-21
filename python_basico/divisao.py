numero_informado = int(input("Digite quantos casos deseja testar: "))

for i in range(numero_informado):
    num1 = float(input("Digite o numerador: "))
    num2 = float(input("Digite o denominador: "))
    if num2 ==0:
        print("Divisão impossível!")
        continue
    divisao = num1/num2
    print(f"Resultado da divisão: {divisao:.2f}")

