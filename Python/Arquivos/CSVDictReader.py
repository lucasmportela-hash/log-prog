import csv
# DictReader transforma cada linha em um dicionario
with open("produtos.csv", "r", encoding="utf-8") as f:
    leitor = csv.DictReader(f)
    for item in leitor:
        # Acesso pelo nome da coluna em vez do indice
        nome = item["nome"]
        preco = item["preco"]
        print(f"{nome} custa R$ {preco}")