import streamlit as st
import pandas as pd
from data_download import descargar_datos

st.set_page_config(page_title="Proyecto Finanzas AAPL", layout="wide")

st.title("Análisis Financiero - AAPL")

st.markdown("Datos históricos de Apple Inc. desde Yahoo Finance")

# Inputs (ya con AAPL por defecto)
ticker = st.text_input("Activo", "AAPL")

inicio = st.date_input("Fecha inicio", pd.to_datetime("2010-01-01"))
fin = st.date_input("Fecha fin", pd.to_datetime("2025-01-01"))

if st.button("Descargar datos"):
    try:
        data = descargar_datos(ticker, inicio, fin)

        st.success("Datos descargados correctamente")

        st.subheader("Vista previa de datos")
        st.dataframe(data.head())

        st.subheader("Serie de precios")
        st.line_chart(data['Precio'])

        st.subheader("Rendimientos logarítmicos")
        st.line_chart(data['Returns'])

        st.subheader("Distribución de rendimientos")
        st.bar_chart(data['Returns'])

    except Exception as e:
        st.error(f"Error: {e}")
