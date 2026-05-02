import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import norm, t
import matplotlib.pyplot as plt
from data_download import descargar_datos

# ---------------------------------------------------
# CONFIG
# ---------------------------------------------------
st.set_page_config(page_title="Proyecto Finanzas AAPL", layout="wide")

st.title("Análisis del activo financiero AAPL")
st.markdown("Proyecto de Métodos Cuantitativos en Finanzas")

# ---------------------------------------------------
# FUNCION VIOLACIONES
# ---------------------------------------------------
def calcular_violaciones(df_rolling, returns_col="Returns"):

    metricas = [
        "VaR_hist_95", "ES_hist_95",
        "VaR_hist_99", "ES_hist_99",
        "VaR_param_95", "ES_param_95",
        "VaR_param_99", "ES_param_99"
    ]

    nombres = {
        "VaR_hist_95": "Histórico VaR 95%",
        "ES_hist_95": "Histórico ES 95%",
        "VaR_hist_99": "Histórico VaR 99%",
        "ES_hist_99": "Histórico ES 99%",
        "VaR_param_95": "Paramétrico VaR 95%",
        "ES_param_95": "Paramétrico ES 95%",
        "VaR_param_99": "Paramétrico VaR 99%",
        "ES_param_99": "Paramétrico ES 99%"
    }

    resultados = []
    total = len(df_rolling)

    for m in metricas:
        viol = (df_rolling[returns_col] < df_rolling[m]).sum()
        pct = viol / total * 100

        resultados.append({
            "Medida de Riesgo": nombres[m],
            "Violaciones": int(viol),
            "Porcentaje (%)": round(pct, 2)
        })

    return pd.DataFrame(resultados)

# ---------------------------------------------------
# INPUTS
# ---------------------------------------------------
ticker = st.text_input("Activo", "AAPL")
inicio = st.date_input("Fecha inicio", pd.to_datetime("2010-01-01"))
fin = st.date_input("Fecha fin", pd.to_datetime("2025-01-01"))

# ---------------------------------------------------
# BOTON
# ---------------------------------------------------
if st.button("Descargar datos"):

    try:
        data = descargar_datos(ticker, inicio, fin)
        returns = data["Returns"]

        st.success("Datos descargados correctamente")

        # =====================================================
        # INCISO A
        # =====================================================
        with st.container():

            st.header("Inciso (a): Datos descargados")
            st.dataframe(data.head())
            st.subheader("Serie de precios")
            st.line_chart(data["Precio"])

        st.divider()

        # =====================================================
        # INCISO B
        # =====================================================
        with st.container():

            st.header("Inciso (b): Rendimientos y estadísticas")

            st.subheader("Rendimientos logarítmicos")
            st.line_chart(returns)

            media = returns.mean()
            sesgo = returns.skew()
            curtosis = returns.kurt()

            st.write(f"Media: {media:.6f}")
            st.write(f"Sesgo: {sesgo:.6f}")
            st.write(f"Exceso de curtosis: {curtosis:.6f}")

            fig, ax = plt.subplots()
            ax.hist(returns, bins=50, density=True)

            mu = returns.mean()
            sigma = returns.std()

            x = np.linspace(returns.min(), returns.max(), 100)
            y = norm.pdf(x, mu, sigma)

            ax.plot(x, y)
            ax.set_title("Distribución de Rendimientos")
            st.pyplot(fig)

        st.divider()

        # =====================================================
        # INCISO C
        # =====================================================
        with st.container():

            st.header("Inciso (c): VaR y ES muestra completa")

            niveles = [0.95, 0.975, 0.99]

            # HISTORICO
            st.subheader("Método Histórico")

            hist = []

            for alpha in niveles:
                var = np.percentile(returns, (1-alpha)*100)
                es = returns[returns <= var].mean()

                hist.append({
                    "Nivel": alpha,
                    "VaR": var,
                    "ES": es
                })

            st.table(pd.DataFrame(hist))

            # PARAMETRICO
            st.subheader("Método Paramétrico")

            mu = returns.mean()
            sigma = returns.std()
            df = 5

            param = []

            for alpha in niveles:

                z = norm.ppf(1-alpha)
                var_n = mu + sigma*z
                es_n = mu - sigma*(norm.pdf(z)/(1-alpha))

                q = t.ppf(1-alpha, df)
                var_t = mu + sigma*q
                es_t = mu - sigma*((t.pdf(q, df)/(1-alpha))*((df+q**2)/(df-1)))

                param.append({
                    "Nivel": alpha,
                    "VaR Normal": var_n,
                    "ES Normal": es_n,
                    "VaR t": var_t,
                    "ES t": es_t
                })

            st.table(pd.DataFrame(param))

            # MONTE CARLO
            st.subheader("Monte Carlo")

            np.random.seed(42)
            sims = 10000

            mc = []

            for alpha in niveles:

                simulados = np.random.normal(mu, sigma, sims)

                var = np.percentile(simulados, (1-alpha)*100)
                es = simulados[simulados <= var].mean()

                mc.append({
                    "Nivel": alpha,
                    "VaR": var,
                    "ES": es
                })

            st.table(pd.DataFrame(mc))

        st.divider()

        # =====================================================
        # INCISO D
        # =====================================================
        with st.container():

            st.header("Inciso (d): Rolling Window 252")

            window = 252
            niveles = [0.95, 0.99]

            resultados = {
                "Returns": [],
                "VaR_hist_95": [],
                "ES_hist_95": [],
                "VaR_hist_99": [],
                "ES_hist_99": [],
                "VaR_param_95": [],
                "ES_param_95": [],
                "VaR_param_99": [],
                "ES_param_99": []
            }

            for i in range(window, len(returns)):

                datos = returns[i-window:i]

                mu = datos.mean()
                sigma = datos.std()

                resultados["Returns"].append(returns.iloc[i])

                for alpha in niveles:

                    var_h = np.percentile(datos, (1-alpha)*100)
                    es_h = datos[datos <= var_h].mean()

                    z = norm.ppf(1-alpha)
                    var_p = mu + sigma*z
                    es_p = mu - sigma*(norm.pdf(z)/(1-alpha))

                    if alpha == 0.95:
                        resultados["VaR_hist_95"].append(var_h)
                        resultados["ES_hist_95"].append(es_h)
                        resultados["VaR_param_95"].append(var_p)
                        resultados["ES_param_95"].append(es_p)

                    else:
                        resultados["VaR_hist_99"].append(var_h)
                        resultados["ES_hist_99"].append(es_h)
                        resultados["VaR_param_99"].append(var_p)
                        resultados["ES_param_99"].append(es_p)

            df_rolling = pd.DataFrame(resultados)
            df_rolling.index = returns.index[window:]

            st.line_chart(df_rolling)

        st.divider()

        # =====================================================
        # INCISO E
        # =====================================================
        with st.container():

            st.header("Inciso (e): Violaciones")

            tabla = calcular_violaciones(df_rolling)

            st.table(tabla)
            st.bar_chart(tabla.set_index("Medida de Riesgo"))

        st.divider()

        # =====================================================
        # INCISO F
        # =====================================================
        with st.container():

            st.header("Inciso (f): VaR con volatilidad móvil")

            rolling_std = returns.rolling(252).std()

            q95 = norm.ppf(0.05)
            q99 = norm.ppf(0.01)

            var95 = q95 * rolling_std
            var99 = q99 * rolling_std

            df_vol = pd.DataFrame({
                "Returns": returns,
                "VaR 95%": var95,
                "VaR 99%": var99
            }).dropna()

            st.line_chart(df_vol)

            viol95 = (df_vol["Returns"] < df_vol["VaR 95%"]).sum()
            viol99 = (df_vol["Returns"] < df_vol["VaR 99%"]).sum()

            total = len(df_vol)

            tabla2 = pd.DataFrame({
                "Nivel": ["95%", "99%"],
                "Violaciones": [viol95, viol99],
                "Porcentaje (%)": [
                    round(viol95/total*100, 2),
                    round(viol99/total*100, 2)
                ]
            })

            st.table(tabla2)
            st.bar_chart(tabla2.set_index("Nivel"))

    except Exception as e:
        st.error(f"Error: {e}")
