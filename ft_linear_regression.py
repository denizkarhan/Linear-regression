import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

t0, t1 = 0.0, 0.0
saveT0, saveT1, saveAcc = [], [], []
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
    tmp_summ = 0.0

    for i in range(len(km)):
        tmp_diff = estimatePrice(km[i]) - float(price[i])
        tmp_diff *= tmp_diff
        tmp_summ += tmp_diff
    return (tmp_summ / len(km))
def updateTeta0(t0, t1):
    global scaledKm, scaledPrice, learningRate
    tmp_summ = 0.0

    for i in range(len(scaledKm)):
        tmp_summ += estimatePrice(scaledKm[i]) - float(scaledPrice[i])
    return learningRate * (tmp_summ / len(scaledKm))
def updateTeta1(t0, t1):
    global scaledKm, scaledPrice, learningRate
    tmp_summ = 0.0

    for i in range(len(scaledKm)):
        tmp_summ += (estimatePrice(scaledKm[i]) - float(scaledPrice[i])) * float(scaledKm[i])
    return learningRate * (tmp_summ / len(scaledKm))
def modelPredict():
    global t0, t1
    global saveT0, saveT1
    global km, price

    normalizeData(km, price)
    mse = meanSquareError(km, price)
    sharpness = mse
    while abs(sharpness) > mse * 0.00001:
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

def getAcc(km, price, t0, t1):
    totalPredict = sum([abs((t0 + t1 * km[i]) - price[i]) for i in range(len(km))])
    return 1 - totalPredict / sum(price)
def saveWeights(t0, t1):
    global saveT0, saveT1
    global km, price, saveAcc

    t1 = (max(price) - min(price)) * t1 / (max(km) - min(km))
    t0 = min(price) + ((max(price) - min(price)) * t0) + t1 * (-min(km))
    saveT0.append(t0)
    saveT1.append(t1)
    saveAcc.append(getAcc(km, price, t0, t1))
def regressionPlot():
    global km, price, fileName
    global saveT0, saveT1, saveAcc
    for i in range(len(saveT1)):
        plt.cla()

        plt.title('ft_linear_regression', backgroundcolor='green')
        plt.title('dkarhan', loc = "right")
        plt.xlabel('Mileage', color="blue")
        plt.ylabel('Price', color="blue")

        predictPrice = [(saveT0[i] + n * saveT1[i]) for n in km]
        plt.plot(km, price, 'ro')
        plt.plot(km, predictPrice, color='green')
        plt.axis([0, max(km) * 1.1, min(price) * 0.50, max(price) * 1.25])
        plt.legend([fileName, '\nWeights\nt0: ' + str(saveT0[i])[:6] + ' | t1: ' + str(saveT1[i])[:6] + '\nAcc: ' + str(saveAcc[i])[:10]])
        plt.pause(0.03)
    plt.show()

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

try:
    learningRate = float(input("Learning rate: "))
    if (learningRate <= 0 or learningRate > 1):
        error("Learning rate must be a [0, 1]")
except:
    error("Warning learning rate!")

modelPredict()
regressionPlot()
