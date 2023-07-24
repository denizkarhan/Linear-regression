import os.path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def normalizeData(km, price):
    global normalizeKm, normalizePrice

    for i in range(len(km)):
        normalizeKm.append((float(km[i]) - min(km)) / (max(km) - min(km)))
        normalizePrice.append((float(price[i]) - min(price)) / (max(price) - min(price)))

def estimatePrice(mileage):
    global t0, t1

    return ((t0 + (t1 * float(mileage))))

def meanSquareError(km, price):
    global t0, t1
    tmp_summ = 0.0

    for i in range(len(km)):
        tmp_diff = estimatePrice(km[i]) - float(price[i])
        tmp_diff *= tmp_diff
        tmp_summ += tmp_diff
    return (tmp_summ / (len(km)))

def updateTeta0(t0, t1):
    global learning_rate, normalizeKm, normalizePrice
    tmp_summ = 0.0

    for i in range(len(normalizeKm)):
        tmp_summ += estimatePrice(normalizeKm[i]) - float(normalizePrice[i])
    return (learning_rate * (tmp_summ / (len(normalizeKm))))

def updateTeta1(t0, t1):
    global learning_rate, normalizeKm, normalizePrice
    tmp_summ = 0.0

    for i in range(len(normalizeKm)):
        tmp_summ += (estimatePrice(normalizeKm[i]) - float(normalizePrice[i])) * float(normalizeKm[i])
    return (learning_rate * (tmp_summ / len(normalizeKm)))

def modelPredict():
    global t0, t1
    global km, price

    normalizeData(km, price)
    mse = meanSquareError(km, price)
    sharpness = mse

    while sharpness > 0.000001 or sharpness < -0.000001:
        t0 -= updateTeta0(t0, t1)
        t1 -= updateTeta1(t0, t1)
        tempMse = mse
        mse = meanSquareError(km, price)
        sharpness = mse - tempMse

    t1 = (max(price) - min(price)) * t1 / (max(km) - min(km))
    t0 = min(price) + ((max(price) - min(price)) * t0) + t1 * (-min(km))

def regressionPlot(km, price, t0, t1):
    plt.title('ft_linear_regression')
    plt.xlabel('Mileage')
    plt.ylabel('Price')

    plt.plot(km, price, 'ro')
    plt.plot([min(km), max(km)], [estimatePrice(min(km)), estimatePrice(max(km))])
    plt.axis([min(km) - abs(max(km) * 0.1), max(km) + abs(max(km) * 0.1), min(price) - abs(max(price) * 0.1), max(price) + abs(max(price) * 0.1)])

    plt.show()

data = pd.read_csv('data.csv')

t0, t1 = 0.0, 0.0
learning_rate = 0.1

km, price = data['km'], data['price']
normalizeKm, normalizePrice = [], []

modelPredict()
regressionPlot(km, price, t0, t1)
