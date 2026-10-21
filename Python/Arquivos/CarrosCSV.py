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
    leitor = csv.DictReader(arquivo, delimiter= ":")
with open("carros.csv", "r", newline="", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for carro in leitor:
        marca = carro["marca"]
        modelo = carro["modelo"]
        ano = carro["ano"]
        print(f"Marca: {marca}, Modelo: {modelo}, Ano: {ano}")