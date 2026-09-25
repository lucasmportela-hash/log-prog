# Construa um programa/página onde o usuário irá criar uma classe com nome, idade e
# altura (em centímetros). O programa dirá se a pessoa é maior ou menor de idade.
class Dados:
    def __init__(self, Nome, Idade, Altura):
        self.Nome = Nome
        self.Idade = Idade
        self.Altura = Altura
    def Verificar(self):
        if self.Idade >= 18:
            return ("Maior de idade")
        else:
            return ("Menor de idade")
Nome = str (input("Digite seu nome: "))
Idade = int (input("Digite sua idade: "))
Altura = float(input("Digite sua altura: "))
Pessoa = Dados(Nome, Idade, Altura)
print(f"{Nome} você tem {Altura} e é {Pessoa.Verificar()}")