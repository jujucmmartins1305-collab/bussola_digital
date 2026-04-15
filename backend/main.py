import chatbot
import os
def start():
    print('Olá! Bem-vindo ao Bússola Digital')
    nome = input("Qual seu nome? ")
    
    print(f"\nMuito prazer, {nome}!")
    os.system("cls")
    print("O que gostaria de aprender hoje com seu guia digital?\n")
    
    print("1- Segurunça digita")
    print("2- cidadania online")
    print("3- Prevenção de incidentes digitaos")
    print("4- Criação de senhas seguras \n")
    escolha = input("Digite o numero do topico: ")

    
    while True:
        texto_usuario = input("\nVocê: ")

        if "C:/" in texto_usuario or "AppData" in texto_usuario:
            continue

        if texto_usuario.lower() in ["sair", "tchau", "sair()"]:
            print(f"{nome}: Volte sempre!")
            break

        resposta = chatbot.buscandoconhecimento(nome, texto_usuario)
        print(f"Chatbot: {resposta}")
        print(f"\nMais alguma dúvida?")

if __name__ == "__main__":
    start()