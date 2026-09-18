senha = input("Digite a senha que deseja criar: ")

while True:
    senha_informada = input("Agora digite a senha para acessar: ")
    if senha_informada != senha:
        print("Senha inválida, tente novamente!")
    else:
        print("Acesso concedido!")
        break