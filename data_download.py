import yfinance as yf
import pandas as pd
import numpy as np

def descargar_datos(ticker="AAPL", inicio="2010-01-01", fin="2025-01-01"):
    data = yf.download(ticker, start=inicio, end=fin)

    if data.empty:
        raise ValueError("No se pudieron descargar datos. Revisa el ticker.")

    
    if 'Adj Close' in data.columns:
        precio_col = 'Adj Close'
    elif 'Close' in data.columns:
        precio_col = 'Close'
    else:
        raise ValueError("No se encontró columna de precios válida.")

    data = data[[precio_col]].rename(columns={precio_col: 'Precio'})

    # Rendimientos logarítmicos
    data['Returns'] = np.log(data['Precio'] / data['Precio'].shift(1))

    data = data.dropna()

    return data
