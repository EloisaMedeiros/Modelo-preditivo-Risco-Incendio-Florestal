# Modelo-preditivo-Risco-Incendio-Florestal 👨‍🚒
Este projeto utiliza técnicas de Machine Learning para prever o risco de incêndios florestais com base em coordenadas geográficas, dados temporais e índices meteorológicos.

## Sobre o Projeto

A aplicação utiliza um modelo de classificação treinado com o algoritmo **K-Nearest Neighbors (KNN)** para analisar variáveis ambientais e determinar a probabilidade de ocorrência de fogo em determinadas áreas.

A interface foi desenvolvida em **Streamlit**, proporcionando uma ferramenta interativa e de fácil uso para análise de dados meteorológicos.

### 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **ML Framework:** Scikit-Learn
* **Interface:** Streamlit
* **Manipulação de Dados:** Pandas & Numpy
* **Dataset:** Forest Fires (UCI Machine Learning Repository)

### Variáveis Analisadas
**O modelo leva em consideração diversos fatores, incluindo:

  * **Coordenadas Espaciais: Posição X e Y no mapa;**
  * **Índices FWI: FFMC, DMC, DC e ISI (componentes do sistema de classificação de perigo de incêndio florestal);**
  * **Condições Meteorológicas: Temperatura, Umidade Relativa (RH), Velocidade do Vento e Chuva.**

### Autores
**Eloisa Medeiros da Silva**
**Giovana Yngrid Duarte Ribeiro**
**Rafael Dimitri Queiroga da Silva**
