import os
print(os.getcwd())
import backend.chatbot as chatbot




def start():
    print('Olá! Bem-vindo ao Bussola Digital')
    nome = input("Qual seu nome? ")


    
    print(f"{os.linesep}Muito prazer, {nome}!")
    print("O que gostaria de aprender hoje com seu guia digital")

    while True:
        texto_usuario = input("")
        resposta = chatbot.buscandoconhecimento(nome,texto_usuario)
    
        print(resposta)
if __name__ == "__main__":
    start()

