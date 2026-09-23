class Livro:

    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f"Titulo do livro: {self.titulo}, Autor do livro: {self.autor}, Ano de publicação: {self.ano_publicacao}"

    def emprestar(self):
        self.disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis


livro1 = Livro("Aprendendo Python", "John Doe", 2022)
livro2 = Livro("Data Science Fundamentals", "Jane Smith", 2020)
livro3 = Livro("Python Cookbook", "Samuel Developer", 2019)
livro4 = Livro("Algoritmos e Estruturas de Dados", "Alice Programadora", 2020)

livro3.emprestar()

