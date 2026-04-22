import tkinter as tk

app = tk.Tk()
app.title("BUSSOLA DIGITAL") 
app.geometry("700x500")
tk.Label(app, text="Guia digital").pack()
 
def resposta_botao():
    nome = entrada_texto.get()
    app['text'] = f"Olá, {nome}"

entrada_texto = tk.Entry(app)
entrada_texto.pack()

tk.Button(app, text="Segurança Digital", command=resposta_botao).pack()


app.mainloop()