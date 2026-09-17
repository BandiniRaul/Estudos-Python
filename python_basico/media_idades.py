total_idades = 0
quantidade_idade = 0

while True:
    idade = int(input("Digite uma idade: "))
    if idade < 0:
        break
    total_idades += idade
    quantidade_idade += 1

media_idade = str(total_idades/quantidade_idade)
print("Média de Idades: " + media_idade)