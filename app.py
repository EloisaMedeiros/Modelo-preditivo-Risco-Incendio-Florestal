import streamlit as st
import pickle
import numpy as np
import pandas as pd

# --- DICIONÁRIOS "CHUMBADOS" (A GAMBIARRA) ---
# Baseado na ordem alfabética do LabelEncoder
MONTH_MAP = {
    'apr': 0, 'aug': 1, 'dec': 2, 'feb': 3, 'jan': 4, 'jul': 5, 
    'jun': 6, 'mar': 7, 'may': 8, 'nov': 9, 'oct': 10, 'sep': 11
}

DAY_MAP = {
    'fri': 0, 'mon': 1, 'sat': 2, 'sun': 3, 'thu': 4, 'tue': 5, 'wed': 6
}
# --- FIM DA GAMBIARRA ---


# --- Carregar o modelo ---
try:
    with open('knn_model.pkl', 'rb') as f:
        knn = pickle.load(f)
except FileNotFoundError:
    st.error("Erro: Arquivo 'knn_model.pkl' não encontrado.")
    st.stop()

# --- Interface do Usuário ---
st.set_page_config(layout="wide")
st.title('🔥 Modelo Preditivo de Risco de Incêndio 🔥')

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Localização e Data")
    # Usar as chaves do dicionário como opções
    month = st.selectbox('Mês', options=list(MONTH_MAP.keys()))
    day = st.selectbox('Dia da Semana', options=list(DAY_MAP.keys()))
    X = st.number_input('Coordenada X (1 a 9)', min_value=1, max_value=9, value=7, step=1)
    Y = st.number_input('Coordenada Y (2 a 9)', min_value=2, max_value=9, value=4, step=1)

with col2:
    st.header("Índices de Fogo (FWI)")
    FFMC = st.number_input('FFMC (18.7 a 96.2)', min_value=18.0, max_value=97.0, value=91.5, format="%.1f")
    DMC = st.number_input('DMC (1.1 a 291.3)', min_value=1.0, max_value=300.0, value=130.1, format="%.1f")
    DC = st.number_input('DC (7.9 a 860.6)', min_value=7.0, max_value=900.0, value=807.1, format="%.1f")
    ISI = st.number_input('ISI (0.0 a 56.1)', min_value=0.0, max_value=60.0, value=7.5, format="%.1f")

with col3:
    st.header("Condições Meteorológicas")
    temp = st.number_input('Temperatura (°C)', min_value=2.0, max_value=34.0, value=21.3, format="%.1f")
    RH = st.number_input('Umidade Relativa (%)', min_value=15, max_value=100, value=35, step=1)
    wind = st.number_input('Velocidade do Vento (km/h)', min_value=0.0, max_value=10.0, value=2.2, format="%.1f")
    rain = st.number_input('Chuva (mm)', min_value=0.0, max_value=7.0, value=0.0, format="%.1f")

if st.button('**Analisar Risco de Incêndio**', use_container_width=True):
    try:
        # --- 1. Processar os Inputs (usando os dicionários) ---
        month_encoded = MONTH_MAP[month]
        day_encoded = DAY_MAP[day]

        # --- 2. Montar o array de features ---
        features = [
            X, Y, month_encoded, day_encoded, FFMC, DMC,
            DC, ISI, temp, RH, wind, rain
        ]
        final_features = np.array(features).reshape(1, -1)

        # --- 3. Fazer a Previsão ---
        prediction = knn.predict(final_features)
        probability = knn.predict_proba(final_features)
        prob_fire = probability[0][1] * 100

        if prediction[0] == 1:
            st.error(f'**RISCO DE FOGO DETECTADO!** (Probabilidade: {prob_fire:.2f}%)', icon="🔥")
        else:
            st.success(f'**CONDIÇÃO SEGURA.** (Probabilidade de Fogo: {prob_fire:.2f}%)', icon="✅")

    except Exception as e:
        st.error(f"Erro durante a previsão: {e}")