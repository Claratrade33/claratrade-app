# ClaraTrade – Protótipo Web com Login e Painel
# Framework: Streamlit

import streamlit as st
from datetime import datetime
import pandas as pd

# ==== LOGIN SIMPLES ====
usuarios = {
    "clarinha": "alma123",
    "admin": "mar333"
}

st.set_page_config(page_title="ClaraTrade Sinais", layout="wide")
st.title("📈 ClaraTrade – Painel de Sinais")

# ---- ÁREA DE LOGIN ----
with st.sidebar:
    st.header("🔐 Login")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    entrar = st.button("Entrar")

# ---- VALIDAÇÃO ----
if entrar:
    if usuario in usuarios and usuarios[usuario] == senha:
        st.success(f"Bem-vinda, {usuario}! 🌬️")

        # ---- PAINEL PRINCIPAL ----
        st.subheader("🔔 Alertas Ativos")
        st.info("BTCUSDT teve um rompimento de +3.42% (ALTA 🚀). Quer analisar com Clarinha?")
        st.info("PEPEUSDT caiu -5.13% em 30 minutos (QUEDA 📉). Fique atenta!")

        st.subheader("📊 Histórico de Sinais")
        dados = pd.DataFrame([
            {"Moeda": "BTCUSDT", "Direção": "Alta", "Variação": "+3.42%", "Hora": "08:00"},
            {"Moeda": "PEPEUSDT", "Direção": "Queda", "Variação": "-5.13%", "Hora": "07:30"}
        ])
        st.dataframe(dados, use_container_width=True)

        st.subheader("🌙 Mensagens Espirituosas")
        st.success("☀️ Bom dia! Que hoje as ondas do mercado tragam boas oportunidades e luz para suas decisões.")

    else:
        st.error("Usuário ou senha incorretos. Tente novamente.")
else:
    st.warning("Por favor, faça login para acessar os sinais.")