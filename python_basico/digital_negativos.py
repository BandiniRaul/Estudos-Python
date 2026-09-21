negativos = 0
n = int(input("Digite um valor inteiro: "))

matriz = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        matriz[i][j] = int(input(f"Elemento [{i},{j}] "))

print("\nMatriz formatada: ")
for i in range(n):
    for j in range(n):
        print(matriz[i][j], end= " ")
    print()

print("\nDiagonal principal:")
for i in range(n):
    for j in range(n):
        if matriz[i] == matriz[j]:
            print(matriz[i][j], end= " ")
        elif matriz[i][j] < 0:
            negativos += 1

print("\nQuantidade de negativos: ",negativos)

