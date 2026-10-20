f = open("dados.txt", "w")
f.write("teste")
f.close() # Se der erro na linha anterior, isso nunca executa
with open("dados.txt", "w") as f:
    f.write("teste")
# Fechado automaticamente ao sair da indentação