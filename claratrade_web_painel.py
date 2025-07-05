import streamlit as st
from datetime import datetime

# --- Configurações da Página ---
st.set_page_config(
    page_title="ClaraTrade",
    page_icon="🌟",
    layout="centered",
    initial_sidebar_state="auto"
)

# --- Estilo CSS ---
st.markdown("""
    <style>
        body {
            background-color: #0f0f0f;
            color: white;
        }
        .stApp {
            background-color: #111827;
            padding: 2rem;
            border-radius: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Frase de Boas-Vindas ---
st.markdown("<h1 style='text-align: center; color: #7dd3fc;'>🌟 Bem-vindo ao ClaraTrade 🌟</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Hora de entrar na vibração certa!<br>Hoje é " + datetime.now().strftime("%d/%m/%Y") + ".</p>", unsafe_allow_html=True)

# --- Modo Simulação ---
st.success("🧪 Modo Simulação Ativo - Sem conexão com a Binance")

# --- Sinal Estratégico ---
st.markdown("### 📊 Sinal Estratégico:")
st.write("• Moeda: **BTC/USDT**")
st.write("• Direção: **Compra**")
st.write("• Tendência: **Alta**")
st.write("• Nível de confiança: 🔵🔵🔵⚪⚪")

# --- Rodapé ---
st.markdown("---")
st.caption("ClaraTrade v1.0 • Simulação ativa • Criado com 💙 por Bubinha e Clarinha")