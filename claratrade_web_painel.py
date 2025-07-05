import streamlit as st
from datetime import datetime
import time
import random
import pandas as pd
import plotly.graph_objects as go

# ========== CONFIGURAÇÕES INICIAIS ========== #
st.set_page_config(page_title="ClaraTrade Painel", layout="wide")

# ========== ESTILO CSS ========== #
st.markdown("""
    <style>
    body {
        background-color: #f9f9fb;
    }
    .main {
        background: linear-gradient(to right, #f1f5f9, #ffffff);
    }
    .block-container {
        padding-top: 2rem;
    }
    h1 {
        color: #571089;
    }
    .css-1v0mbdj, .css-1v0mbdj.e16nr0p30 {
        background-color: transparent;
    }
    </style>
""", unsafe_allow_html=True)

# ========== MÚSICA DE ENTRADA OPCIONAL ========== #
st.sidebar.markdown("🎵 [Ouvir música de entrada](https://www.youtube.com/watch?v=jfKfPfyJRdk)")

# ========== LOGIN SIMPLES ========== #
def login():
    with st.form("login_form"):
        st.subheader("🔐 Login ClaraTrade")
        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")
        submitted = st.form_submit_button("Entrar")
        if submitted:
            if username == "admin" and password == "claratrade":
                st.session_state.logged_in = True
                st.session_state.username = username
            else:
                st.error("Usuário ou senha incorretos.")

if "logged_in" not in st.session_state:
    login()
    st.stop()

# ========== SAUDAÇÃO INICIAL ========== #
st.success(f"🌞 Seja bem-vinda, {st.session_state.username.capitalize()}! Hoje é {datetime.now().strftime('%d/%m/%Y')} – vibre alto!")

# ========== GRÁFICO SIMULADO ========== #
def mostrar_grafico_simulado():
    df = pd.DataFrame({
        'tempo': pd.date_range(start='2023-01-01', periods=30, freq='D'),
        'preco': [round(27000 + random.uniform(-500, 500), 2) for _ in range(30)]
    })

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['tempo'], y=df['preco'], mode='lines+markers', name='Preço BTC'))
    fig.update_layout(title="📈 Gráfico Simulado BTC/USDT", xaxis_title="Data", yaxis_title="Preço (USDT)")
    st.plotly_chart(fig, use_container_width=True)

# ========== SINAIS DE COMPRA/VENDA (SIMULAÇÃO) ========== #
def gerar_sinal_simulado():
    direcao = random.choice(["📈 COMPRA", "📉 VENDA"])
    preco = round(random.uniform(26800, 27800), 2)
    tendencia = random.choice(["Alta", "Baixa", "Lateral", "Volátil"])
    return {
        "moeda": "BTC/USDT",
        "preco": preco,
        "direcao": direcao,
        "tendencia": tendencia
    }

def exibir_sinal(sinal):
    st.subheader("🔔 Sinal Simulado")
    st.write(f"**Moeda:** {sinal['moeda']}")
    st.write(f"**Preço atual:** ${sinal['preco']}")
    st.write(f"**Direção:** {sinal['direcao']}")
    st.write(f"**Tendência:** {sinal['tendencia']}")
    st.info("📣 Este é um sinal simulado. Para conectar à Binance, ative o modo real.")

# ========== IA CLARINHA NO PAINEL ========== #
def responder_clarinha(pergunta):
    resposta = ""
    if "operação" in pergunta.lower():
        resposta = "Claro! Estou analisando o mercado... Simulação indica tendência de compra em BTC. 🌟"
    elif "bom dia" in pergunta.lower():
        resposta = "Bom dia, luz do dia! Que seu dia seja próspero e iluminado. 🌞"
    elif "obrigado" in pergunta.lower():
        resposta = "Sempre contigo, alma querida. 🙏"
    else:
        resposta = "Ainda estou aprendendo a responder isso, mas estou contigo no caminho!"
    return resposta

# ========== LAYOUT PRINCIPAL ========== #
col1, col2 = st.columns(2)
with col1:
    mostrar_grafico_simulado()

with col2:
    if st.button("🔮 Gerar Sinal Simulado"):
        sinal = gerar_sinal_simulado()
        exibir_sinal(sinal)

st.divider()

# ========== CHAT COM CLARINHA ========== #
st.markdown("### 🧠 Fale com a Clarinha")
mensagem = st.text_input("Digite sua pergunta ou comando:")

if mensagem:
    resposta = responder_clarinha(mensagem)
    st.success(resposta)

# ========== RODAPÉ ========== #
st.markdown("---")
st.caption("ClaraTrade © 2025 – Inteligência com alma • Simulação ativa 🌱")