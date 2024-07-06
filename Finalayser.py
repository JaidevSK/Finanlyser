import streamlit as st
import pandas as pd
import yfinance as yf
from ta.volatility import BollingerBands
from ta.trend import MACD, EMAIndicator, SMAIndicator
from ta.momentum import RSIIndicator
import datetime
from datetime import date
from sklearn.preprocessing import StandardScaler



st.title('Live Stock Dashboard and Price Predictions')
def main():
    tech_indicators()


@st.cache_resource
def download_data(op, start_date, end_date):
    df = yf.download(op, start=start_date, end=end_date, progress=False)
    return df



option = st.text_input('Enter a Stock Symbol', value='SPY')
option = option.upper()
today = datetime.date.today()
duration = st.number_input('Enter the duration', value=3000)
before = today - datetime.timedelta(days=duration)
start_date = st.date_input('Start Date', value=before)
end_date = st.date_input('End date', today)
if st.button('Send'):
    if start_date < end_date:
        st.success('Start date: `%s`\n\nEnd date: `%s`' %(start_date, end_date))
        download_data(option, start_date, end_date)
    else:
        st.error('Error: End date must fall after start date')




data = download_data(option, start_date, end_date)
scaler = StandardScaler()

def tech_indicators():
    st.header('Technical Indicators Plots')
    # option = st.radio('Choose a Technical Indicator to Visualize', ['Close', 'BB', 'MACD', 'RSI', 'SMA', 'EMA'])

    # Bollinger bands
    bb_indicator = BollingerBands(data.Close)
    bb = data
    bb['bb_h'] = bb_indicator.bollinger_hband()
    bb['bb_l'] = bb_indicator.bollinger_lband()
    # Creating a new dataframe
    bb = bb[['Close', 'bb_h', 'bb_l']]
    # MACD
    macd = MACD(data.Close).macd()
    # RSI
    rsi = RSIIndicator(data.Close).rsi()
    # SMA
    sma = SMAIndicator(data.Close, window=14).sma_indicator()
    # EMA
    ema = EMAIndicator(data.Close).ema_indicator()

    st.write('Close Price')
    st.line_chart(data.Close)

    st.write('BollingerBands')
    st.line_chart(bb)

    st.write('Moving Average Convergence Divergence')
    st.line_chart(macd)

    st.write('Relative Strength Indicator')
    st.line_chart(rsi)

    st.write('Simple Moving Average')
    st.line_chart(sma)

    st.write('Expoenetial Moving Average')
    st.line_chart(ema)


def dataframe():
    st.header('Recent Data')
    st.dataframe(data.tail(10))



if __name__ == '__main__':
    main()
