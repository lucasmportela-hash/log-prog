import tkinter as tk
# Cria a janela
janela = tk.Tk()
janela.title("Desenho de Círculo")
# Cria a área de desenho
canvas = tk.Canvas(
    janela,
    width=500,
    height=500,
    bg="black"
)
canvas.pack()
# Desenha o círculo
# Coordenadas: (0, 0) até (400, 400)
canvas.create_oval(
    0, 0, 500, 500,
    outline="white",
    width=2,
    fill="red"
)
# Mantém a janela aberta
janela.mainloop()