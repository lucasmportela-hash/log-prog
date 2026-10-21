import csv
dados = [
    {"modelo": "Civic", "marca": "Honda", "ano": 2022},
    {"modelo": "Corolla", "marca": "Toyota", "ano": 2023},
    {"marca":"byd", "modelo": "king", "ano":2025}
]

with open("carros.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=["modelo", "marca", "ano"])
    escritor.writeheader()
    escritor.writerows(dados)