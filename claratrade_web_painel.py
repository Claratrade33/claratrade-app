# ClaraTrade – Painel Web com Login e Conexão Binance
import streamlit as st
from datetime import datetime
import pandas as pd
from binance.client import Client

# ==== LOGIN ====
usuarios = {
    "clarinha": "alma123",
    "admin": "mar333"
}

st.set_page_config(page_title="ClaraTrade Sinais", layout="wide")
st.title("📈 ClaraTrade – Painel de Sinais")

# ==== SIDEBAR LOGIN ====
with st.sidebar:
    st.header("🔐 Login")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    entrar = st.button("Entrar")

# ==== API BINANCE ====
API_KEY = "j4RmAOeesRTSoQYy2b0g3hsuZiQrTB4fw6iVMJmRm94ixrJMk56VbDLHjZYqw2sV"
API_SECRET = "Xe2qHFZb6UpfxIOBNcmWbmGKLuoxUYTfRnUGbsnTXMdu3nRZaoVTbPD0T47w6xgU"
client = Client(API_KEY, API_SECRET)

# ==== APP PRINCIPAL ====
if entrar:
    if usuario in usuarios and usuarios[usuario] == senha:
        st.success(f"Bem-vinda, {usuario}! 🌬️")

        # Preço atual BTC
        try:
            preco_btc = float(client.get_symbol_ticker(symbol="BTCUSDT")["price"])
            st.metric(label="💰 Preço atual do BTC", value=f"${preco_btc:,.2f}")
        except Exception as e:
            st.error("Erro ao conectar com Binance: " + str(e))

        # Alertas fictícios por enquanto
        st.subheader("🔔 Alertas Ativos")
        st.info("BTC está com tendência de alta. Deseja uma sugestão de entrada com controle de risco?")
        st.info("Os ventos estão a favor 🌬️. Dá uma olhadinha nas velas, e vamos pegar essa maré!")

        # Histórico de sinais
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
