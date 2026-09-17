from enum import Enum
class Produtos (Enum):
    CODE_1 = 5.00
    CODE_2 = 3.50
    CODE_3 = 4.80
    CODE_4 = 8.90
    CODE_5 = 7.32

codigo_produto = str(input("Digite o código do produto que deseja comprar: "))
quantidade_produto = int(input("Digite a quantidade desse produto que deseja comprar: "))

produto = Produtos[codigo_produto].value
valor_unitario = produto
valor_total = valor_unitario * quantidade_produto

print(f"Valor total dos produtos: R${valor_total:.2f}")
