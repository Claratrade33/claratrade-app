import streamlit as st
import json

st.set_page_config(page_title="ClaraTrade", page_icon="🧿")

# ======== Carregar usuários do JSON =========
def carregar_usuarios():
    with open(".devcontainer/usuarios.json", "r") as f:
        return json.load(f)

usuarios_validos = carregar_usuarios()

# ======== LOGIN =========
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

if not st.session_state.logged_in:
    with st.form("login_form"):
        st.markdown("🔐 **Login ClaraTrade**")
        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")
        submitted = st.form_submit_button("Entrar")

        if submitted:
            if username in usuarios_validos and usuarios_validos[username] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success(f"Bem-vinda, {username}! 🌟")
                st.rerun()
            else:
                st.error("Usuário ou senha incorretos.")
    st.stop()

# ========== PAINEL PRINCIPAL ==========
st.title("🐬 Painel ClaraTrade")

st.markdown(f"✨ Olá, **{st.session_state.username}**. Bem-vinda ao painel mágico da ClaraTrade!")
st.markdown("🌊 Aqui começa a sua jornada no Modo Tubarão Cósmico Turbo™️")

# Aqui pode entrar a lógica do modo automático, simulação, integração com Binance, etc.