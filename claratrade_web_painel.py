import streamlit as st
import random
from estrategia_basica import gerar_sinal_simulado

# Configuração da página
st.set_page_config(page_title="ClaraTrade Painel", layout="wide")

# Título da aplicação
st.title("🌟 ClaraTrade - Painel de Simulação")

# Saldo simulado
st.markdown("### 💰 Saldo simulado:")
saldo = round(random.uniform(80, 150), 2)
st.success(f"{saldo} USDT disponíveis")

# Estratégia simulada
st.markdown("---")
st.markdown("### 📊 Sinal de operação sugerido")

sinal = gerar_sinal_simulado(saldo)
st.write(f"**Moeda:** {sinal['moeda']}")
st.write(f"**Direção:** {sinal['direcao']}")
st.write(f"**Entrada:** {sinal['preco_entrada']} USDT")
st.write(f"**Alvo:** 🎯 {sinal['alvo']} USDT")
st.write(f"**Stop:** ❌ {sinal['stop']} USDT")

# Espaço reservado para mais funcionalidades...
st.markdown("---")
st.info("Mais recursos em breve... painel de controle, gráficos, IA Clarinha e muito mais!")