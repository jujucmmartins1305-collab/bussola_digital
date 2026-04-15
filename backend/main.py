import chatbot

def start():
    print('Olá! Bem-vindo ao Bússola Digital')
    nome = input("Qual seu nome? ")
    
    print(f"\nMuito prazer, {nome}!")
    print("O que gostaria de aprender hoje com seu guia digital?")

    while True:
        texto_usuario = input("\nVocê: ")

        if "C:/" in texto_usuario or "AppData" in texto_usuario:
            continue

        if texto_usuario.lower() in ["sair", "tchau", "sair()"]:
            print(f"{nome}: Volte sempre!")
            break

        resposta = chatbot.buscandoconhecimento(nome, texto_usuario)
        print(f"Chatbot: {resposta}")

if __name__ == "__main__":
    start()