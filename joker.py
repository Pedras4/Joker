import tkinter as tk

def iniciar_jogo():
    print("Jogo iniciado!")

# Janela principal
janela = tk.Tk()
janela.title("Joker")
janela.geometry("500x400")
janela.configure(bg="#5414b4")

# Carregar imagem do título
imagem_titulo = tk.PhotoImage(file="Jokerr.png")
imagem_titulo = imagem_titulo.subsample(2, 2)

label_imagem = tk.Label(
    janela,
    image=imagem_titulo,
    bg="#5414b4"
)
label_imagem.pack(pady=40)

# Botão iniciar
botao_iniciar = tk.Button(
    janela,
    text="Iniciar Jogo",
    font=("Arial", 14),
    bg="white",
    fg="black",
    width=20,
    height=5,
    command=iniciar_jogo
)
botao_iniciar.pack()

janela.mainloop()