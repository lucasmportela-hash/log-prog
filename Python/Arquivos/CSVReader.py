import csv
with open("alunos.csv", "r", encoding="utf-8") as f:
    leitor = csv.reader(f, delimiter=",")
    # Pula a linha do cabeçalho
    cabecalho = next(leitor)
    for linha in leitor:
        nome = linha[0]
        nota = linha [1]
        print(f"Aluno: {nome} | Nota: {nota}")