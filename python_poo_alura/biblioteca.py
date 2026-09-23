from livro import Livro

livro_biblioteca = Livro("1984", "George Orwell", 1949)
print(livro_biblioteca.disponivel)
livro_biblioteca.emprestar()
print(livro_biblioteca.disponivel)


ano_especifico = 2020
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}")