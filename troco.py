NOTAS = [200, 100, 50, 20, 10, 5, 2]
montante_total = 0

def validar_notas(notas_recebidas):
    return notas_recebidas in NOTAS

valor_produto = float(input("Digite o valor do produto: "))
quantidade_produto = int(input("Quantidade de produtos comprados: "))
valor_total_produto = valor_produto * quantidade_produto
print("Valor total da compra: R$" + (f"{valor_total_produto: .2f}"))


while montante_total < valor_total_produto:
    notas_recebidas = int(input("Digite com quais notas você irá pagar: "))
    if not validar_notas(notas_recebidas):
        print("Essa nota não é válida, insira uma nota verdadeira: ")
        continue
    print("Notas recebidas!")
    montante_total += notas_recebidas
    print("Valor total de pagamento acumulado: R$" + (f"{montante_total: .2f}"))


def calcular_troco(montante_total, valor_total_produto):
    troco = montante_total - valor_total_produto
    return troco

troco = calcular_troco(montante_total, valor_total_produto)
print(f"Valor do troco: R$ {troco:.2f}")


