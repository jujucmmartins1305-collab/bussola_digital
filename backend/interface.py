import tkinter as tk
from PIL import Image, ImageTk
import chatbot
import os

etapa = "nome"
nome_usuario = ""
pergunta_sem_resposta = ""
app = tk.Tk()
app.title("BÚSSOLA DIGITAL")
app.iconphoto(True, ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), "bussola_digital.png")).resize((64, 64))))
app.geometry("700x500")
app.config(bg="#F0F0F0")

frame_lateral = tk.Frame(app, bg="#F0F0F0", width=280)
frame_lateral.pack(side="left", fill="y")

frame_direito = tk.Frame(app, bg="white")
frame_direito.pack(side="left", fill="both", expand=True)

frame_topo = tk.Frame(frame_direito, bg="white", pady=10)
frame_topo.pack(fill="x")



tk.Label(frame_topo, text="Você está em um ambiente seguro — tire suas dúvidas à vontade!", bg="white", fg="#041139", font=("Arial", 10)).pack(pady=5)

img = Image.open(os.path.join(os.path.dirname(__file__), "bussola_digital.png")).convert("RGBA").resize((165, 100))
logo = ImageTk.PhotoImage(img)

tk.Label(frame_lateral, image=logo, bg="lightblue").pack(pady=20)
tk.Label(frame_lateral, text="Navegando com consciência,\nprotegendo sua essência.", bg="lightblue", fg="#1E1E1E", font=("Arial", 8), justify="center").pack(pady=5)

canvas = tk.Canvas(frame_direito, bg="white")
scrollbar = tk.Scrollbar(frame_direito, command=canvas.yview)
frame_chat = tk.Frame(canvas, bg="white")
canvas.configure(yscrollcommand=scrollbar.set)

frame_input = tk.Frame(frame_direito, bg="#F0F0F0")
frame_input.pack(fill="x", side="bottom", padx=10, pady=10)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((0, 0), window=frame_chat, anchor="nw", width=canvas.winfo_width())

def redimensionar(event):
    canvas.itemconfig(1, width=event.width)
canvas.bind("<Configure>", redimensionar)   
   

lbl_boas_vindas = tk.Label(frame_chat, text="Olá! Bem-vindo ao Bússola Digital! Qual é o seu nome?", bg="#EAEAEA", wraplength=300, justify="left")
lbl_boas_vindas.pack(anchor="w", padx=10, pady=5)

def atualizar_scroll(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame_chat.bind("<Configure>", atualizar_scroll)

def enviar(event=None):
    global etapa, nome_usuario, pergunta_sem_resposta
    mensagem = campo_mensagem.get()
    if mensagem.strip() != "":
        palavra_chave = mensagem.strip().lower()
        if palavra_chave == "tchau" or palavra_chave == "fim": 
            lbl_usuario = tk.Label(frame_chat, text=mensagem, bg="#1A2B5E", fg="white", wraplength=300, justify="right", padx=8, pady=4)
            lbl_usuario.pack(anchor="e", padx=100, pady=5)
            
            lbl_bot = tk.Label(frame_chat, text="Até logo! O Bússola Digital agradece seu contato. Fechando...", bg="#EAEAEA", wraplength=400, justify="left")
            lbl_bot.pack(anchor="w", padx=25, pady=5)
            
            campo_mensagem.delete(0, tk.END)
            
            app.after(2000, app.destroy)
            return
    
    if mensagem.strip() != "":

        lbl_usuario = tk.Label(frame_chat, text=mensagem, bg="#1A2B5E", fg="white", wraplength=300, justify="right", padx=8, pady=4)
        lbl_usuario.pack(anchor="e", padx=100, pady=5)
        
        campo_mensagem.delete(0, tk.END)
    
        if etapa == "nome":
            nome_usuario = mensagem
            etapa = "chat"
            lbl_boas_vindas = tk.Label(frame_chat, text=f"Olá, {nome_usuario}! Bem-vindo ao Bússola Digital! O que você gostaria de aprender hoje?", bg="#EAEAEA", wraplength=400, justify="left")
            lbl_boas_vindas.pack(anchor="w", padx=10, pady=5)

        elif etapa == "aprendendo":
            caminho_db = os.path.join(os.path.dirname(__file__), "database.txt")
            with open(caminho_db, "a+", encoding="utf-8") as conhecimento:
                conhecimento.write("\n" + pergunta_sem_resposta.strip())
                conhecimento.write("\nChatbot: " + mensagem.strip())
            
            lbl_bot = tk.Label(frame_chat, text="Obrigado! Agora eu já sei como responder isso.", bg="#EAEAEA", wraplength=400, justify="left")
            lbl_bot.pack(anchor="w", padx=25, pady=5)
            
            etapa = "chat"
        
        elif etapa == "chat":
            pergunta_sem_resposta = mensagem
            app.after(500, lambda: resposta_bot(chatbot.buscandoconhecimento("Usuário", mensagem)))

def resposta_bot(texto):
    global etapa
    lbl_bot = tk.Label(frame_chat, text=texto, bg="#EAEAEA", wraplength=400, justify="left")
    lbl_bot.pack(anchor="w", padx=25, pady=5)
    if texto == "Me desculpe, não sei o que falar. Você pode me dar uma dica de como responder? ":
        etapa = "aprendendo"

campo_mensagem = tk.Entry(frame_input)
campo_mensagem.pack(side="left", fill="x", expand=True, padx=(0, 5), ipady=8)

campo_mensagem.bind("<Return>", lambda event: enviar())

botao_enviar = tk.Button(frame_input, text="Enviar", width=10, command=enviar)
botao_enviar.pack(side="right")

app.mainloop()