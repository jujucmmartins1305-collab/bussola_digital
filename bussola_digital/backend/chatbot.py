def buscandoconhecimento(nome, texto):
    with open("database.txt", "a+", encoding="utf-8") as conhecimento:
        conhecimento.seek(0)
        
        while True:
            viu = conhecimento.readline()

            if viu != "":
                if viu.strip().lower() == texto.strip().lower():
                    proxima = conhecimento.readline()
                    if ":" in proxima:
                        return proxima.split(":", 1)[1].strip()
            else:
                print("Me desculpe, não sei o que falar.")
                resposta_user = input("Você pode me dar uma dica de como responder? ")
                
                conhecimento.write("\n" + texto.strip())
                conhecimento.write("\nChatbot: " + resposta_user.strip())
                
                return "Obrigado! Agora eu já sei como responder isso."