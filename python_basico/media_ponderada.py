numero_informado = int(input("Digite quantos casos deseja testar: "))

for i in range(numero_informado):
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10

    print(f"Media ponderada: {media:.2f}")