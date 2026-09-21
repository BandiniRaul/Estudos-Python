nome1 = input("Digite o primeiro nome: ")
idade1 = int(input("Digite a primeira idade: "))
nome2 = input("Digite o segundo nome: ")
idade2 = int(input("Digite a segunda idade: "))
media = (idade1 + idade2)/2

print("\nDados da primeira pessoa:")
print(f"Nome: {nome1}\nIdade: {idade1}")
print("\nDados da segunda pessoa:")
print(f"Nome: {nome2}\nIdade: {idade2}")
print(f"\nMedia de idade das duas pessoas é: {media:.1f}")
