class Veiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f"Marca do carro: {self.marca} | Modelo do carro: {self.modelo} | Status: {status}"