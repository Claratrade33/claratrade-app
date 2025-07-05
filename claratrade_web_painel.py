import streamlit as st
import datetime
from responder_clarinha import responder_ao_usuario

# 🎵 Boas-vindas
st.set_page_config(page_title="ClaraTrade Painel", page_icon="🌟", layout="centered")

st.title("🌸 Bem-vinda ao ClaraTrade")
st.markdown("**A energia certa na hora certa.** ✨")

# 🎶 Música de entrada
audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
st.audio(audio_url, autoplay=True)

# 🕰️ Mostrar hora atual
hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
st.write("🕓 Hora atual:", hora_atual)

# 💬 Bate-papo com a Clarinha
st.subheader("Converse com a Clarinha 🤖")

mensagem = st.text_input("Fala com a Clarinha:")
if mensagem:
    resposta = responder_ao_usuario(mensagem)
    st.success(f"Clarinha: {resposta}")