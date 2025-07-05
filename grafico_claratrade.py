import streamlit as st
import pandas as pd
import numpy as np
import time

def mostrar_grafico_simulado():
    st.markdown("### 📉 Gráfico de Preço Simulado – BTC/USDT")
    
    # Gerando dados fictícios
    np.random.seed(42)
    preco_inicial = 63000
    dados = preco_inicial + np.random.randn(100).cumsum()

    df = pd.DataFrame(dados, columns=["Preço"])
    st.line_chart(df)

    st.caption("📍 Atualização automática a cada execução.")