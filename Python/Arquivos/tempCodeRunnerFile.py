import csv
cabecalho = ["marca","modelo","ano"]
with open("carros.csv", "w", encoding="utf-8", newline='') as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames="cabecalho", delimiter=";")
    escritor.writeheader()
    escritor.writerows(dados)