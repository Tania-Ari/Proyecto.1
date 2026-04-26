import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import norm, t
from data_download import descargar_datos

st.set_page_config(page_title="Proyecto Finanzas AAPL", layout="wide")

st.title("Análisis del activo financiero AAPL")

st.markdown("Datos históricos de Apple Inc. desde Yahoo Finance")

ticker = st.text_input("Activo", "AAPL")

inicio = st.date_input("Fecha inicio", pd.to_datetime("2010-01-01"))
fin = st.date_input("Fecha fin", pd.to_datetime("2025-01-01"))

if st.button("Descargar datos"):
    try:
        data = descargar_datos(ticker, inicio, fin)

        st.success("Datos descargados correctamente")

        st.subheader("Vista previa de datos")
        st.dataframe(data.head())

        # Inciso b)
        st.subheader("Estadísticas de los rendimientos")

        mean = data['Returns'].mean()
        skew = data['Returns'].skew()
        kurt = data['Returns'].kurt()

        st.write(f"Media: {mean:.6f}")
        st.write(f"Sesgo: {skew:.6f}")
        st.write(f"Exceso de curtosis: {kurt:.6f}")

        # Inciso c) 
        st.subheader("Value at Risk y Expected Shortfall histórico")

        returns = data['Returns']
        niveles = [0.95, 0.975, 0.99]

        resultados_hist = []

        for alpha in niveles:
            var = np.percentile(returns, (1 - alpha) * 100)
            es = returns[returns <= var].mean()

            resultados_hist.append({
                "Nivel de confianza": alpha,
                "VaR": var,
                "ES": es
            })

        tabla_hist = pd.DataFrame(resultados_hist)
        st.table(tabla_hist)

        # 🔥 INCISO 3 - VaR PARAMÉTRICO (NORMAL y t-STUDENT)
        st.subheader("Value at Risk y Expected Shortfall paramétrico")

        mu = returns.mean()
        sigma = returns.std()

        resultados_param = []

        df = 5  # grados de libertad para t-student

        for alpha in niveles:
            z = norm.ppf(1 - alpha)

            # VaR Normal
            var_normal = mu + sigma * z

            # ES Normal
            es_normal = mu - sigma * (norm.pdf(z) / (1 - alpha))

            # VaR t-Student
            t_quantile = t.ppf(1 - alpha, df)
            var_t = mu + sigma * t_quantile

            # ES t-Student
            es_t = mu - sigma * ((t.pdf(t_quantile, df) / (1 - alpha)) * ((df + t_quantile**2) / (df - 1)))

            resultados_param.append({
                "Nivel": alpha,
                "VaR Normal": var_normal,
                "ES Normal": es_normal,
                "VaR t-Student": var_t,
                "ES t-Student": es_t
            })

        tabla_param = pd.DataFrame(resultados_param)
        st.table(tabla_param)

        # 🔹 Gráficas
        st.subheader("Serie de precios")
        st.line_chart(data['Precio'])

        st.subheader("Rendimientos logarítmicos")
        st.line_chart(data['Returns'])

        st.subheader("Distribución de rendimientos")
        st.bar_chart(data['Returns'])

    except Exception as e:
        st.error(f"Error: {e}")
