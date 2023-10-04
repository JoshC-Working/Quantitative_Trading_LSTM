import math
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
import yfinance as yf
import datetime
import os
import pdb
import threading
import queue


class ModelTrainer(threading.Thread):
    def __init__(self, num,  *args, x_train, y_train, num_cells_layer1, num_batch_size, num_epochs, errorQueue=None, modelQueue=None, lock=None, x_test, y_test):
        threading.Thread.__init__(self)
        self.x_train = x_train
        self.y_train = y_train
        self.num_cells_layer1 = num_cells_layer1
        self.num_batch_size = num_batch_size
        self.num_epochs = num_epochs
        self.errorQueue = errorQueue
        self.modelQueue = modelQueue
        self.lock = lock
        self.num = num
        self.x_test = x_test
        self.y_test = y_test

    def run(self):
        model = Sequential()

        j = self.x_train.shape[1]
        model.add(LSTM(self.num_cells_layer1,
                  return_sequences=False, input_shape=(j, 1)))
        model.add(Dense(25))
        model.add(Dense(1))
        model.compile(optimizer='adam', loss='mean_squared_error')

        model.fit(self.x_train, self.y_train,
                  batch_size=self.num_batch_size, epochs=self.num_epochs)

        predictions = model.predict(self.x_test)
        predictions = scaler.inverse_transform(predictions)

        rmse = np.sqrt(np.mean((self.y_test - predictions)**2))

        self.lock.acquire()
        print(f"Lock acquired by {self.name}")

        modelQueue.put(rmse)
        modelQueue.put(model)
        modelQueue.put(int(self.num))

        print(f"Lock acquired by {self.num}")
        self.lock.release()


# Define some constants
# Enter the stock symbol that we would like to do research on
stock = "NVR"

# Hyperparameters for the training approach
# No. of historical records(days) for the closing price of a day
window_interval = 60
delay = 8  # i.e. the No. of future days that we can do prediction

# Hyperparameters for the Model
num_cells_layer1 = 20
num_cells_layer2 = None
num_batch_size = 1024
num_epochs = 1

# Get the stock quote

start_date = datetime.datetime(2002, 1, 1)
# end_date = datetime.datetime(2019, 12, 17)

####
modelQueue = queue.Queue()
errorQueue = queue.Queue()
lock = threading.Lock()

####
df = yf.download(stock, start=start_date)

data = df[['Close']]
dataset = data.values

# Get the length of training data
# Ratio of Train and Test set is 8:2
training_data_len = math.ceil(len(dataset)*0.8)


# Scale the data by MinMax Method

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(dataset)


# Build Training Set
train_data = scaled_data[0:training_data_len]

x_train = []
y_train = []

for i in range(window_interval+delay, len(train_data)):
    x_train.append(train_data[i-window_interval-delay:i-delay, 0])
    y_train.append(train_data[i, 0])

x_train, y_train = np.array(x_train), np.array(y_train)
i, j = x_train.shape
x_train_reshaped = np.reshape(x_train, (i, j, 1))
x_train_reshaped.shape

# Build Test Set
test_data = scaled_data[training_data_len-window_interval:]
x_test = []
y_test = dataset[training_data_len:,]

for i in range(window_interval, len(test_data)):
    x_test.append(test_data[i-window_interval:i, 0])


x_test = np.array(x_test)
i, j = x_test.shape
x_test = np.reshape(x_test, (i, j, 1))

# Build the LSTM Model

########################################################################
threadList = []
for i in range(10):
    threadList.append(ModelTrainer(i, x_train=x_train, y_train=y_train, x_test=x_test, y_test=y_test, num_cells_layer1=num_cells_layer1,
                                   num_batch_size=num_batch_size, num_epochs=num_epochs, errorQueue=None, modelQueue=modelQueue, lock=lock))

    threadList[i].start()

for i in range(10):
    threadList[i].join()

modelList = [0] * 10
while modelQueue.qsize() > 0:
    tmpRMSE = modelQueue.get()
    tmpModel = modelQueue.get()
    index = modelQueue.get()
    modelList[index - 1] = [tmpModel, tmpRMSE]

# print(modelList)
modelList = np.array(modelList)

posMinError = np.argmin(modelList[:, 1])

modelList[posMinError, 0].save(stock+'_model')
