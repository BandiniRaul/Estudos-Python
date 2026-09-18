def verificar_quadrante(tupla):
        x,y = tupla
        if x > 0 and y > 0:
            return "Q1"
        elif x < 0 and y > 0:
            return "Q2"
        elif x < 0 and y < 0:
            return "Q3"
        else:
            return "Q4"

while True:
    x = int(input("Digite a cordenada x: "))
    y = int(input("Digite a cordenada y: "))
    if x or y is None:
         break
    tupla = (x,y)
    print (verificar_quadrante(tupla))
    
