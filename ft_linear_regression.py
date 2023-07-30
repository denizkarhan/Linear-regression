import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

t0, t1 = 0.0, 0.0
t0s, t1s = [], []
scaledKm, scaledPrice = [], []

def error(msg):
    print(msg)
    exit(1)
def normalizeData(km, price):
    global scaledKm, scaledPrice

    for i in range(len(km)):
        scaledKm.append((float(km[i]) - min(km)) / (max(km) - min(km)))
        scaledPrice.append((float(price[i]) - min(price)) / (max(price) - min(price)))
def estimatePrice(mileage):
    global t0, t1
    return (t0 + (t1 * float(mileage)))
def meanSquareError(km, price):
    # MSE = (1/n) * Σ(yᵢ - ȳ)²
    # y -> bagimli degisken (data.csv - fiyat)
    # ȳ -> t0 + t1 * milage (tahmin edilen fiyat)
    global t0, t1
    tmp_summ = 0.0

    for i in range(len(km)):
        tmp_diff = estimatePrice(km[i]) - float(price[i])
        tmp_diff *= tmp_diff
        tmp_summ += tmp_diff
    return (tmp_summ / (len(km)))
def updateTeta0(t0, t1):
    global scaledKm, scaledPrice
    tmp_summ = 0.0

    for i in range(len(scaledKm)):
        tmp_summ += estimatePrice(scaledKm[i]) - float(scaledPrice[i])
    return tmp_summ / len(scaledKm)
def updateTeta1(t0, t1):
    global scaledKm, scaledPrice
    tmp_summ = 0.0

    for i in range(len(scaledKm)):
        tmp_summ += (estimatePrice(scaledKm[i]) - float(scaledPrice[i])) * float(scaledKm[i])
    return tmp_summ / len(scaledKm)
def modelPredict():
    global t0, t1
    global t0s, t1s
    global km, price

    normalizeData(km, price)
    mse = meanSquareError(km, price)
    sharpness = mse
    while sharpness > 0.000001 or sharpness < -0.000001:
        if (abs(sharpness) > 1):
            saveWeights(t0, t1)
        t0 -= updateTeta0(t0, t1)
        t1 -= updateTeta1(t0, t1)
        tempMse = mse
        mse = meanSquareError(km, price)
        sharpness = mse - tempMse

    t1 = (max(price) - min(price)) * t1 / (max(km) - min(km))
    t0 = min(price) + ((max(price) - min(price)) * t0) + t1 * (-min(km))

    save = open('thetaValues.txt', 'w')
    save.write(str(t0) + "," + str(t1))
def saveWeights(t0, t1):
    global t0s, t1s
    global km, price

    t1 = (max(price) - min(price)) * t1 / (max(km) - min(km))
    t0 = min(price) + ((max(price) - min(price)) * t0) + t1 * (-min(km))
    t0s.append(t0)
    t1s.append(t1)
def regressionPlot():
    global km, price, fileName
    global t0s, t1s
    for i in range(len(t1s)):
        plt.cla()

        plt.title('ft_linear_regression', backgroundcolor='green')
        plt.title('dkarhan', loc = "right")
        plt.xlabel('Mileage', color="purple")
        plt.ylabel('Price', color="purple")

        predictPrice = [(t0s[i] + n * t1s[i]) for n in km]
        plt.plot(km, price, 'ro')
        plt.plot(km, predictPrice, color='green')
        plt.axis([0, max(km) * 1.1, min(price) * 0.50, max(price) * 1.25])
        plt.legend([fileName, '\nWeights\nt0: ' + str(t0s[i])[:8] + '\nt1: ' + str(t1s[i])[:8]], loc ="upper right")
        plt.pause(0.1)

try:
    fileName = input("Enter the data set: ")
    data = pd.read_csv(fileName)
    if len(data['km']) < 2 or len(data['price']) < 2:
        error("Not enough data found!")
    km, price = data['km'], data['price']
except FileNotFoundError:
    error("File not found!")
except IOError:
    error("File could not be opened!")

modelPredict()
regressionPlot()
