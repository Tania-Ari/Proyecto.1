import yfinance as yf
import pandas as pd
import numpy as np

def descargar_datos(ticker="AAPL", inicio="2010-01-01", fin="2025-01-01"):
    """
    Descarga datos históricos desde Yahoo Finance
    y calcula rendimientos logarítmicos.
    """

    data = yf.download(ticker, start=inicio, end=fin)

    # Validación
    if data.empty:
        raise ValueError("No se pudieron descargar datos. Revisa el ticker.")

    # Seleccionar precio ajustado
    data = data[['Adj Close']]
    data = data.rename(columns={'Adj Close': 'Precio'})

    # Rendimientos logarítmicos
    data['Returns'] = np.log(data['Precio'] / data['Precio'].shift(1))

    data = data.dropna()

    return data
