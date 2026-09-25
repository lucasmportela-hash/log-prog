# Construa uma página/programa cadastrando cinco funcionários de uma escola, sendo
# que dois deles são professores. Todos os funcionários terão cadastrados seus nomes e
# salários e, os professores, terão cadastrados a disciplina às quais lecionam.
class Funcionarios:
    def __init__(self, Nome, Salario, Disciplina, Cargo):
        self.Nome = Nome
        self.Salario = Salario
        self.Cargo = Cargo
        if (Cargo == "professor"):
            self.Disciplina = Disciplina
for i in range(5):
    Nome = str(input(f"Digite seu nome {i+1}: "))
    Salario = float(input("Digite seu salario: "))
    Cargo = str(input("Digite seu cargo: ").lower())
    if (Cargo == "professor"):
        Disciplina = str(input("Digite sua disciplina: "))
    else:
        Disciplina = ""
    Funcionario = Funcionarios(Nome, Salario, Cargo, Disciplina)
    if Salario >= 2000:
        print(f"Salario Acima de 2000! {Nome}")
    if (Disciplina == "Matemática"):
       print(f"{Nome} Você leciona Matemática!") 
    print(f"{Nome} você é {Cargo} e tem um salário de {Salario:.2f}")
