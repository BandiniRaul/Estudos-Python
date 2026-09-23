class Restaurante:
    def __init__(self, nome, categoria, capacidade=0, nota_avaliacao=0.0, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
        self.ativo = ativo

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.capacidade} | {self.nota_avaliacao}'


restaurante_formatado = Restaurante(nome='Bom Sabor', categoria='Tradicional', capacidade=50, nota_avaliacao=4.9)
print(restaurante_formatado)