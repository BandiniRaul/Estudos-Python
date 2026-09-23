class Cliente:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

    def __str__(self):
        return f"{self.nome}, {self.idade}, {self.email}, {self.telefone}"


cliente1 = Cliente(nome="Raul", idade=20, email="raul@lapaza.com", telefone="(43)99850-5755")
cliente2 = Cliente(nome="João", idade=20, email="joão@lapaza.com", telefone="(43)93324-8672")
cliente3 = Cliente(nome="Mazini", idade=22, email="mazini@lapaza.com", telefone="(43)98792-0639")

print(cliente1)
print(cliente2)
print(cliente3)
