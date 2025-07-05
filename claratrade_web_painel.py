import streamlit as st
from clarinha_ia import responder_ao_usuario

st.set_page_config(page_title="ClaraTrade", layout="wide")

# Mensagem de entrada
st.markdown("## 🌟 Bem-vinda, alma linda!")
st.success("🎶 Sinta essa vibração: você está no ClaraTrade. Tudo aqui está em ressonância com o seu sucesso.")

# Simulador de saldo fictício
saldo = 92.00
st.metric("💰 Saldo simulado (USDT)", f"${saldo:.2f}")

# Chat com a IA Clarinha
st.markdown("---")
st.markdown("### 💬 Converse com a Clarinha:")

mensagem = st.text_input("Digite algo para a IA Clarinha:")
if mensagem:
    resposta = responder_ao_usuario(mensagem)
    st.info(resposta)

# Modo simulado ativado
st.markdown("---")
st.warning("🔁 Modo Simulação ativado - Nenhuma operação real será feita na Binance.")

st.markdown("##### 🌈 Painel operando em sintonia com a sua intenção.")