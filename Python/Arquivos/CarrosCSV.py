import csv

dados = [
    {"marca":"byd", "modelo": "king", "ano":2025},
]
cabecalho = ["marca","modelo","ano"]
with open("alunos.csv", "w", encoding="utf-8", newline='') as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames="cabecalho", delimiter=";")
    escritor.writeheader()
    escritor.writerows(dados)