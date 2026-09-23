class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f"Modelo do carro: {self.modelo}, Cor do carro: {self.cor}, Ano do carro: {self.ano}"


carro1 = Carro(modelo="Mustang", cor="Preto,", ano=2013)
print(carro1)