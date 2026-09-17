valor = input("Digite o valor do raio: ")

try:
    r = float(valor)
    area = 3.14159 * pow(r,2)
    print(f"{area:.3f}")
except ValueError:
    print("Digite um valor decimal válido")

