from veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, marca, modelo, portas, cor):
        super().__init__(marca, modelo)
        self.portas = portas
        self.cor = cor

    def __str__(self):
        return f"{super().__str__()} - Portas: {self.portas} - Cor: {self.cor}"

    def ligar(self):
        print(f"O carro {self.modelo} está ligado")
        