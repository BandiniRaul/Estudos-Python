from carro import Carro
from moto import Moto


carro_1 = Carro("Toyota", "Corolla", 4, "Preto")
carro_2 = Carro("Volkswagen", "Gol", 2, "Prata")
carro_3 = Carro("Honda", "Civic", 4, "Branco")

moto_1 = Moto("Honda", "CB 500", "Casual")
moto_2 = Moto("Yamaha", "MT-03", "Esportiva")
moto_3 = Moto("BMW", "R 1250 GS", "Espotiva")

print(f"Carro 1: {carro_1.marca} {carro_1.modelo}, Cor: {carro_1.cor}, Portas: {carro_1.portas}")
print(f"Carro 2: {carro_2.marca} {carro_2.modelo}, Cor: {carro_2.cor}, Portas: {carro_2.portas}")
print(f"Carro 3: {carro_3.marca} {carro_3.modelo}, Cor: {carro_3.cor}, Portas: {carro_3.portas}")
print()
print(moto_1)
print(moto_2)
print(moto_3)