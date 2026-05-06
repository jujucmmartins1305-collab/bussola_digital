import tkinter as tk

app = tk.Tk()
app.title("BUSSOLA DIGITAL") 
app.geometry("700x500")
app.config(bg="lightblue")
tk.Label(app, text="GUIA DIGITAL").pack()

frame_chat = tk.Frame(app, bg="white")
frame_chat.pack(fill="both", expand=True, padx=10, pady=10)

frame_input = tk.Frame(app, bg="lightblue")
frame_input.pack(fill="x", side="bottom", padx=10, pady=10)
compo_mensagem = tk.Entry(frame_input) 
compo_mensagem.pack(side="left", fill="x", expand=True, padx=(0,10), ipady=18)
 


def enviar():
    mensagem = compo_mensagem.get()
    mensagem_enviada = tk.Label(frame_chat, text=mensagem)
    mensagem_enviada.pack(side="right")
    print(mensagem)




botao_enviar = tk.Button(frame_input, text="Enviar", width=10, command=enviar)
botao_enviar.pack(side="right")



app.mainloop()