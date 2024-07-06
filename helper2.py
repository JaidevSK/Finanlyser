############################################

# All Code in One Page

############################################

#!/usr/bin/env python3
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


date_today = datetime.date.today()

ticker = "BTC-INR"

def predict_tom(ticker):
    stock_ticker = yf.Ticker(ticker)
    df=stock_ticker.history(start='2001-01-01', end= date_today, actions=False)
    df=df.drop(['Open','High','Volume','Low'],axis=1)
    data=df.values
    train_len=math.ceil(len(data)*0.90)
    min_max_scalar=MinMaxScaler(feature_range=(0,1))
    scaled_data=min_max_scalar.fit_transform(data)
    train_data=scaled_data[0:train_len,:]
    interval=60
    x_train=[]
    y_train=[]
    for i in range(interval,len(train_data)):
        x_train.append(train_data[i-interval:i,0])
        y_train.append(train_data[i,0])
    x_train,y_train=np.array(x_train),np.array(y_train)
    x_train=np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))
    model=Sequential()
    model.add(LSTM(50,return_sequences=True,input_shape=(x_train.shape[1],1)))
    model.add(LSTM(units=50))
    model.add(Dense(50))
    model.add(Dense(1))
    model.compile(optimizer="adam",loss="mean_squared_error")
    history=model.fit(x_train,y_train,batch_size=64,epochs=10)
    test_data=scaled_data[train_len-interval:,:]
    x_test=[]
    y_test=data[train_len:,:]
    for i in range(interval,len(test_data)):
        x_test.append(test_data[i-interval:i,0])
    x_test=np.array(x_test)
    x_test=np.reshape(x_test,(x_test.shape[0],x_test.shape[1],1))
    predictions=model.predict(x_test)
    predictions=min_max_scalar.inverse_transform(predictions)
    train_data=df[0:train_len]
    valid_data=df[train_len:]
    #rmse 
    rmse=np.sqrt(np.mean(predictions-y_test)**2)
    df_test=stock_ticker.history(start='2001-01-01', end=date_today, actions=False)
    df_test=df_test.drop(['Open','High','Volume','Low'],axis=1)
    test_value=df_test[-60:].values
    test_value=min_max_scalar.transform(test_value)
    test=[]
    test.append(test_value)
    test=np.array(test)
    test=np.reshape(test,(test.shape[0],test.shape[1],1))
    tomorrow_prediction=model.predict(test)
    tomorrow_prediction=min_max_scalar.inverse_transform(tomorrow_prediction)
    return tomorrow_prediction,rmse