def buscandoconhecimento(nome, texto):
    import os
    from difflib import SequenceMatcher

    def parecido(a, b):
        return SequenceMatcher(None,a.lower(), b.lower()).ratio()

    caminho = os.path.join(os.path.dirname(__file__), "database.txt")
    with open(caminho, "a+", encoding="utf-8") as conhecimento:
                    conhecimento.seek(0)
        
                    
                    while True:
                        viu = conhecimento.readline()

                        if viu == "":
                            break
                        if parecido(viu.strip(),texto.strip()) > 0.8:
                            proxima = conhecimento.readline()
                            if ":" in proxima:
                                return proxima.split(":", 1)[1].strip()
                            else:
                                break
    return "Me desculpe, não sei o que falar. Você pode me dar uma dica de como responder? "