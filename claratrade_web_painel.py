# claratrade_web_painel.py
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="ClaraTrade Painel", layout="wide")

# Boas-vindas
st.markdown("<h1 style='text-align: center; color: #80dfff;'>🌟 Bem-vindo ao ClaraTrade 🌟</h1>", unsafe_allow_html=True)
st.markdown("---")

# Frase de boas-vindas
st.markdown(f"<h3 style='text-align: center; color: #ffffff;'>Hora de entrar na vibração certa! Hoje é {datetime.now().strftime('%d/%m/%Y')}.</h3>", unsafe_allow_html=True)

# Modo Simulação
st.success("🧪 Modo Simulação Ativo - Sem conexão com a Binance")

# Sinal de exemplo
st.markdown("### 📊 Sinal Estratégico:")
st.markdown("- Moeda: **BTC/USDT**")
st.markdown("- Direção: **Compra**")
st.markdown("- Tendência: **Alta**")
st.markdown("- Nível de confiança: 🔵🔵🔵⚪⚪")

# Rodapé
st.markdown("---")
st.markdown("<p style='text-align: center;'>Desenvolvido com 💜 por Clarinha - Projeto ClaraTrade</p>", unsafe_allow_html=True)