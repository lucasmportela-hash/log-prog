# Construa um programa que o usuário digitará o nome e a idade de dez
# pessoas e o programa escreverá o nome do usuário mais novo.
Lista = []
for i in range(10):
    Nome = input(f"Digite seu nome {i + 1}: ")
    Idade = int(input("Digite a sua idade: "))
    Lista.append([Nome, Idade])
MaisNovo = Lista[0][1]
for i in range(1, len(Lista)):
    if Lista[i][1] < MaisNovo:
        MaisNovo = Lista[i][1]
print(f"{MaisNovo} é o mais novo!")
