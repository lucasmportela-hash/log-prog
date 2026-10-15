# 5: Módulo de Triagem de Recrutamento
# Desenvolva um programa que simule a coleta e armazenamento de dados de 5
# candidatos a vagas de emprego:
# ● Cada candidato deve ser representado por um dicionário com os campos:
# "nome", "idade", "telefone", "email" e "formacao".
# ● Todos os candidatos aprovados na triagem devem ser armazenados em uma
# lista principal chamada banco_candidatos.
# ● Regra de negócio: Candidatos com idade inferior a 18 anos não podem
# participar do processo. Caso a idade informada seja menor que 18, o
# programa deve rejeitar o registro, exibir uma mensagem de recusa e não
# inserir o candidato na lista.
# ● Ao término da entrada de dados, o sistema deve iterar sobre
# banco_candidatos e exibir um relatório contendo: Nome, E-mail e Formação  
# de cada candidato apto.
banco_candidatos = [] 
for i in range (2):
    candidato = {}
    candidato["nome"] = input(f"Digite o seu nome candidato {i+1} : ")
    candidato["idade"] = int(input("Digite a sua idade: "))
    if candidato["idade"] < 18:
        print("Idade inválida")
        continue
    candidato["telefone"] = (input("Informe o seu telefone: "))
    candidato["email"] = (input("Informe o seu email: "))
    candidato["formacao"] = (input("Qual a sua formação: "))
    banco_candidatos.append(candidato)
for candidato in banco_candidatos:
    print("Nome:", candidato["nome"])
    print("E-mail:", candidato["email"])
    print("Formação:", candidato["formacao"])
print("Total de candidatos aptos:", len(banco_candidatos))