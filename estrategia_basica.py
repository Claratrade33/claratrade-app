import random

def gerar_sinal_simulado(saldo):
    moeda = random.choice(["BTC/USDT", "ETH/USDT", "PEPE/USDT", "SOL/USDT"])
    direcao = random.choice(["Compra", "Venda"])
    preco_entrada = round(random.uniform(100, saldo), 2)
    alvo = round(preco_entrada * (1 + random.uniform(0.01, 0.03)), 2)
    stop = round(preco_entrada * (1 - random.uniform(0.01, 0.02)), 2)

    return {
        "moeda": moeda,
        "direcao": direcao,
        "preco_entrada": preco_entrada,
        "alvo": alvo,
        "stop": stop
    }