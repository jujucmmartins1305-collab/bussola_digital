def buscandoconhecimento(nome, texto):
    with open("database.txt" , "a+", encoding="utf-8") as conhecimento:
        conhecimento.seek(0)
        while True:
            proximalinha = ""
            viu =conhecimento.readline()
            if viu != "":
                if texto.replace("Usuario: ","") == "Tchau":
                    print(nome+ ": Volte sempre!")
                    return "Fim"
                elif viu.strip() == texto.strip():
                    proximalinha = conhecimento.redline()
                if "chatbot: " in proximalinha:
                    return proximalinha
            else:
                print("Me desculpe, não sei o que falar")
                conhecimento.write("\n" + texto)
                resposta_user = input("Voce pode me da uma dica?\n")
                conhecimento.write("\n" + "Chatbot: "+resposta_user)
                return "Hum... Obrigado por compreender!"