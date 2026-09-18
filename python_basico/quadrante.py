import matplotlib.pyplot as plt

lista_tuplas: list[tuple[int, int]] = []

def verificar_quadrante(tupla: tuple[int, int]):
    x, y = tupla
    if x > 0 and y > 0:
        return "Q1"
    elif x < 0 and y > 0:
        return "Q2"                        
    elif x < 0 and y < 0:
        return "Q3"
    else:
        return "Q4"


def mostrar_pontos(tuplas: list[tuple[int, int]]):
    if not tuplas:
        return

    pontos_x, pontos_y = zip(*tuplas)
    plt.axhline(0, color="black", linewidth=0.8)
    plt.axvline(0, color="black", linewidth=0.8)
    plt.scatter(pontos_x, pontos_y, color="blue")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Pontos no plano cartesiano")
    plt.grid(True)
    plt.axis("equal")
    plt.show()

while True:
    x = input("Digite a cordenada x: ")
    y = input("Digite a cordenada y: ")
    if x == "" or y == "":
        print("Valor vazio, digite um número inteiro!")
        break
    tupla = (int(x),int(y))
    lista_tuplas.append(tupla)
    print("Pontos adicionados no plano cartesiano: ", tupla, verificar_quadrante(tupla))
        
for t in lista_tuplas:
    print(t)

mostrar_pontos(lista_tuplas)