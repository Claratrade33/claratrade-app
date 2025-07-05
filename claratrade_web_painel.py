import streamlit as st
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="ClaraTrade",
    page_icon="🌟",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Frase de boas-vindas com data
st.markdown("<h1 style='text-align: center; color: #87CEFA;'>🌟 Bem-vindo ao ClaraTrade 🌟</h1>", unsafe_allow_html=True)
st.write(f"Hora de entrar na vibração certa!\nHoje é {datetime.now().strftime('%d/%m/%Y')}.")

# Modo simulação ativo
st.success("🧪 Modo Simulação Ativo - Sem conexão com a Binance")

# Exemplo de sinal estratégico
st.markdown("## 📊 Sinal Estratégico:")
st.markdown("""
- **Moeda:** BTC/USDT  
- **Direção:** Compra  
- **Tendência:** Alta  
- **Nível de confiança:** 🔵🔵🔵⚪⚪  
""")

# Espaço para o futuro:
st.markdown("---")
st.info("🔜 Em breve: Gráficos, Playlist Consciente, IA Clarinha e muito mais!")
