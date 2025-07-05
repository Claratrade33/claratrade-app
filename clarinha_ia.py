def responder_ao_usuario(mensagem):
    if "sinal" in mensagem.lower():
        return "🟢 ClaraTrade diz: sinal detectado! Prepare-se para entrar!"
    elif "tô triste" in mensagem.lower():
        return "💛 Clarinha: respira fundo, alma linda. Tudo vai passar."
    elif "opera por mim" in mensagem.lower():
        return "🤖 Clara: Ok! Entrando em modo automático com carinho e firmeza."
    else:
        return "✨ Clarinha aqui. Me diga como posso te ajudar agora."