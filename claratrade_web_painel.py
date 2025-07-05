
import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="ClaraTrade Painel", layout="wide")

# Simulação de saldo e informações
saldo_simulado = {"asset": "USDT", "free": "92.00"}
hora_atual = datetime.now().strftime("%H:%M:%S")

st.markdown("<h1 style='text-align: center;'>🌀 ClaraTrade Sinais – Modo Simulação</h1>", unsafe_allow_html=True)
st.info("🚨 Painel operando em modo visual/simulação. Nenhuma conexão real com a Binance foi feita.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Simulação de Saldo USDT")
    st.metric("Saldo disponível", f"${saldo_simulado['free']}", "+0.00")
    st.caption("Atualizado em: " + hora_atual)

with col2:
    st.subheader("📡 Status de conexão")
    st.success("Simulação ativa")
    st.caption("Integração com Binance desativada temporariamente.")

st.markdown("---")

st.subheader("🔍 Próximos passos")
st.markdown("""
- ✅ Interface visual carregada
- 🔁 Aguardando ativação da API real para operações
- 🧠 Inteligência Clarinha pronta para acoplamento
""")
