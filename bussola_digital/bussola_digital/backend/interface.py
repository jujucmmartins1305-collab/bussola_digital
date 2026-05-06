import tkinter as tk

app = tk.Tk()
app.title("BUSSOLA DIGITAL")
app.geometry("700x500")
app.config(bg="lightblue")

tk.Label(app, text="GUIA DIGITAL", bg="lightblue", font=("Arial", 12, "bold")).pack(pady=5)


frame_chat = tk.Frame(app, bg="white")
frame_chat.pack(fill="both", expand=True, padx=10, pady=10)

def enviar(event=None):
    mensagem = campo_mensagem.get()
    
    if mensagem.strip() != "":

        lbl_usuario = tk.Label(frame_chat, text=mensagem, bg="#EAEAEA", wraplength=300, justify="right")
        lbl_usuario.pack(anchor="e", padx=10, pady=5)
        
        campo_mensagem.delete(0, tk.END)
    
        app.after(500, lambda: resposta_bot("Olá! Eu sou o assistente da Bússola Digital."))

def resposta_bot(texto):
    lbl_bot = tk.Label(frame_chat, text=texto, bg="#EAEAEA", wraplength=300, justify="left")
    lbl_bot.pack(anchor="w", padx=10, pady=5)

frame_input = tk.Frame(app, bg="lightblue")
frame_input.pack(fill="x", side="bottom", padx=10, pady=10)

campo_mensagem = tk.Entry(frame_input)
campo_mensagem.pack(side="left", fill="x", expand=True, padx=(0, 10), ipady=8)

campo_mensagem.bind("<Return>", lambda event: enviar())

botao_enviar = tk.Button(frame_input, text="Enviar", width=10, command=enviar)
botao_enviar.pack(side="right")

app.mainloop()