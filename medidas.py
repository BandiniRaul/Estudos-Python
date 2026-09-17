a = float(input ("Digite o valor de A: "))
b = float(input ("Digite o valor de B: "))
c = float(input ("Digite o valor de C: "))

dicionario = {"A": a, "B": b, "C": c}


def quadrado(dicionario):
    area_quadrado = str(dicionario["A"] * dicionario["A"])
    return area_quadrado


def triangulo(dicionario):
    area_triangulo = str((dicionario["A"] * dicionario["B"])/2)
    return area_triangulo

def trapezio(dicionario):
    area_trapezio = str((dicionario["A"]+dicionario["B"]) * dicionario["C"]/2)
    return area_trapezio


print("Área do Quadrado: "+quadrado(dicionario))
print("Área do Triângulo: "+triangulo(dicionario))
print("Área do Trapézio: "+trapezio(dicionario))

