texto = input("Digite um texto: ")
def padronizar(texto):
    return texto.lower().strip()
padrao = padronizar(texto)

def vernum(texto):
    return any(char.isdigit() for char in texto)
numero = vernum(texto)

print(padrao)
print(f"Há um número no texto: {numero}")
