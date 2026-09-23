class Musica:
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

    def __str__(self):
        return f"Nome da música: {self.nome}, Nome do artista: {self.artista}, Duração da música: {self.duracao} "


musica1 = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao=248)
musica2 = Musica(nome='The Trooper', artista='Iron Maiden', duracao=245)
musica3 = Musica(nome='Hotel California', artista='Eagles', duracao=390)

print(musica1)