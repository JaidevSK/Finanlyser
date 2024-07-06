import streamlit as st
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import math
import numpy as np
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import LSTM,Dense
from keras import regularizers
from tensorflow.keras.optimizers import Adam,RMSprop,SGD,Adamax
import datetime
from helper2 import *

date_today = datetime.date.today()

# ticker = "BTC-INR"

st.markdown("<h1 style='text-align: center; color: #0000FF;'>Stock Predictor</h1>", unsafe_allow_html=True)
st.markdown(
    """
    This app predicts the stock price of the selected stock for tomorrow.
    """
)



# Build the stock ticker
stock_ticker = st.text_input("Enter the stock ticker", "AAPL")
# Submit
st.markdown("<h3 style='text-align: center; color: #222222;'>Predicted Price</h3>", unsafe_allow_html=True)
tomorrow_price, err = predict_tom(stock_ticker)
tomorrow_price0 = tomorrow_price[0][0]
st.write(f"The predicted price of {stock_ticker} for tomorrow is: ₹{tomorrow_price0}")
st.write(f"The error in prediction is: {err}")
