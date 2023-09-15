import yfinance as yf
import numpy as np
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import os


def get_data(stock, interval, delay):

    df = yf.download(stock)
    df = df[["Close"]]
    df = df[-(interval+delay):]
    dataset = df.values
    return dataset


def dataset_building(interval, delay, scaled_data):

    x_evaluation = []

    for i in range(interval, len(scaled_data)):
        x_evaluation.append(scaled_data[i-interval:i, 0])

    return x_evaluation


def predict_data(stock, interval, delay):

    dataset = get_data("AAPL", interval, delay)

    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(dataset)

    x_evaluation = dataset_building(interval, delay, scaled_data)

    # Transform into Array type and then reshape for Keras Model
    x_evaluation = np.array(x_evaluation)
    x_evaluation = np.reshape(
        x_evaluation, (x_evaluation.shape[0], x_evaluation.shape[1], 1))

    root_dir = os.getcwd()
    path = os.path.join(root_dir, "Resources/"+stock+"_model")

    loaded_model = load_model(path)
    predictions = loaded_model.predict(x_evaluation)
    predictions = scaler.inverse_transform(predictions)

    return predictions


print(predict_data("DHI", 40, 8))
