import tkinter as tk
from tkinter import Image
import random

#perguntas
perguntas = [
    {
        "pergunta": "O numero de elementos da primeira tabela periódica é",
        "opcoes": ["67", "63", "78", "96"],
        "resposta": "63"
    },
    {
        "pergunta": "A resposta de é 7 x 8 é",
        "opcoes": ["56", "48", "64", "78"],
        "resposta": "56"
    },
    {
        "pergunta": "A NBA foi criada em",
        "opcoes": ["1890", "1949", "1969", "1978"],
        "resposta": "1949"
    },
    {
        "pergunta": "Os impulsos nervosos que saem chegam ao cerebro e correm a uma velocidade de",
        "opcoes": ["220 km/h", "270 km/h", "200 km/h", "250 km/h"],
        "resposta": "270 km/h"
    },
    {
        "pergunta": "Quantas cores os olhos distinguem",
        "opcoes": ["20 Milhões", "3 Milhões", "10 Milhões", "45 Milhões"],
        "resposta": "10 Milhões"
    },
    {
        "pergunta": "A Nintendo antes de ser uma empresa de videojogos era uma empresa de",
        "opcoes": ["Cartas", "Carros", "Telefones", "Filmes"],
        "resposta": "Cartas"
    },
    {
        "pergunta": "Na lenda hebraica, Noé conversou com deus, um leão espirrou, e daí nasceu que animal?",
        "opcoes": ["Piriquito", "Lince", "Pomba", "Gato"],
        "resposta": "Gato"
    },
]

#funções
def limpar_tela():
    for widget in janela.winfo_children():
        widget.destroy()

def menu():
    limpar_tela()

    tk.Label(
        janela,
        text="Joker",
        font=("Arial", 22, "bold"),
        bg="#5414b4",
        fg="white"
    ).pack(pady=30)

    tk.Button(
        janela,
        text="Iniciar Jogo",
        font=("Arial", 16),
        width=20,
        height=2,
        command=iniciar_jogo
    ).pack(pady=10)

    tk.Button(
        janela,
        text="Sair",
        font=("Arial", 14),
        width=15,
        command=janela.destroy
    ).pack(pady=10)
    
    foto_vasco = tk.PhotoImage(file="vasco.png") 
    label_vasco = tk.Label(janela, image=foto_vasco, bg="#5414b4")
    label_vasco.place(x=1000, y=450) 

    label_vasco.image = foto_vasco

def iniciar_jogo():
    limpar_tela()

    global label_pergunta, botoes, label_resultado, pergunta_atual

    label_pergunta = tk.Label(
        janela,
        text="",
        font=("Arial", 18, "bold"),
        bg="#5414b4",
        fg="white",
        wraplength=450
    )
    label_pergunta.pack(pady=20)

    frame_botoes = tk.Frame(janela, bg="#5414b4")
    frame_botoes.pack(pady=10)

    botoes = []
    for _ in range(4):
        botao = tk.Button(
            frame_botoes,
            text="",
            font=("Arial", 14),
            width=25,
            height=2
        )
        botao.pack(pady=5)
        botoes.append(botao)

    label_resultado = tk.Label(
        janela,
        text="",
        font=("Arial", 14),
        bg="#5414b4",
        fg="white"
    )
    label_resultado.pack(pady=10)

    tk.Button(
        janela,
        text="Voltar ao Menu",
        command=menu
    ).pack(pady=10)

    mostrar_pergunta()

def mostrar_pergunta():
    global pergunta_atual

    pergunta_atual = random.choice(perguntas)

    label_pergunta.config(text=pergunta_atual["pergunta"])

    respostas = pergunta_atual["opcoes"].copy()
    random.shuffle(respostas)

    for i in range(4):
        botoes[i].config(
            text=respostas[i],
            command=lambda r=respostas[i]: verificar_resposta(r)
        )

def verificar_resposta(resposta):
    if resposta == pergunta_atual["resposta"]:
        label_resultado.config(text="✅ Correto!", fg="lightgreen")
    else:
        label_resultado.config(
            text=f"❌ Errado!",
            fg="red"
        )

    janela.after(1500, proxima_pergunta)

def proxima_pergunta():
    label_resultado.config(text="")
    mostrar_pergunta()

#janela
janela = tk.Tk()
janela.title("Joker")
janela.geometry("500x450")
janela.configure(bg="#5414b4")

menu()

janela.mainloop()
