# Construa um programa que o usuário digitará o nome e a idade de dez
# pessoas e o programa escreverá o nome do usuário mais novo.
Idades = []
Nomes = []
posicaoMaisNovo = 0
for i in range(3):
    Nome = input(f"Digite seu nome {i + 1}: ")
    Nomes.append(Nome)
    Idade = int(input("Digite a sua idade: "))
    Idades.append(Idade)
for i in range(1, 3):
    if Idades[i] < Idades[posicaoMaisNovo]:
        posicaoMaisNovo = i
MaisNovo = Nomes[posicaoMaisNovo]
print(f"{MaisNovo} é o mais novo!")
