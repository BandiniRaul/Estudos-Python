import csv

alunos = [["Raul", 10.0], ["Joao", 5.0], ["Mazini", 7.3]]

with open("alunos.csv", "w", newline="") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(["Nome", "Nota"])
    escritor.writerows(alunos)

with open("alunos.csv", "r") as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    next(leitor)
    for nome, nota in leitor:
        if float(nota) >= 7.0:
            print(nome, nota)

