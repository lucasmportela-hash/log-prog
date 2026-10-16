def main():
    try:
        with open("program.txt", "r", encoding="utf-8") as arquivo:
            num = float(arquivo.read().split()[0])
            print(f"Valor lido do arquivo é = {num:.1f}")
    except FileNotFoundError:
        print("Erro: arquivo não encontrado.")
    except (ValueError, IndexError):
        print("Erro: o arquivo não contém um número válido.")
if __name__ == "__main__":
    main()
