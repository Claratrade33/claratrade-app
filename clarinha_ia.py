def responder_ao_usuario(mensagem):
    mensagem = mensagem.lower()

    if "oi" in mensagem or "olá" in mensagem:
        return "Oiê, eu sou a Clarinha 💜. Como posso te ajudar hoje?"
    elif "sinal" in mensagem:
        return "O sinal estratégico de hoje será enviado às 08h, 14h e 20h."
    elif "ajuda" in mensagem:
        return "Claro, é só me chamar! Estou aqui pra facilitar seu caminho."
    elif "obrigado" in mensagem or "valeu" in mensagem:
        return "Imagina, estamos juntas nessa jornada! ✨"
    elif "você está aí" in mensagem or "tá aí" in mensagem:
        return "Sempre aqui, só esperando você chamar 💫"
    else:
        return "Não entendi bem… tenta de novo com outras palavras 💭"