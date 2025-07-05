def responder_ao_usuario(mensagem):
    mensagem = mensagem.lower()

    if "oi" in mensagem or "olá" in mensagem:
        return "Oiê, eu sou a Clarinha 🌸 Estou aqui para te ajudar com seus trades!"
    elif "sinal" in mensagem:
        return "O sinal estratégico de agora é BTC/USDT em COMPRA com tendência de alta 🚀"
    elif "ajuda" in mensagem:
        return "Claro, é só me chamar! Posso te mostrar sinais, mensagens espirituais e insights do mercado."
    elif "obrigado" in mensagem or "valeu" in mensagem:
        return "Imagina, estamos juntas nessa caminhada 🌈"
    elif "você está aí" in mensagem or "tá aí" in mensagem:
        return "Sempre aqui, só esperando seu comando 🌟"
    else:
        return "Não entendi bem… tenta me dizer de outro jeitinho? 💭"

# Exemplo de uso:
if __name__ == "__main__":
    pergunta = input("Fala com a Clarinha: ")
    resposta = responder_ao_usuario(pergunta)
    print("Clarinha:", resposta)