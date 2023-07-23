import os.path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def normalizeData():
    # Veri setindeki her bir kilometre ve fiyat değerini
    # minKm ile maxKm ve minPrice ile maxPrice arasında 0-1 arasında yeniden değerlendiriyor
    
    # Örneğin kilometre değeri 10000 olsun maxKm 25000 minKm 5000 ise
    # 10000 kilometrenin normalize değeri (10000 - 5000) / (25000 - 5000) = 0.25

    # Bu değerler gradyan fonksiyonunun kayıp değerleri azaltarak teta0 ve teta1 katsayılarının bulunmasına yardım ediyor

    global km, price
    global normalizeKm, normalizePrice
    global min_km, max_km, min_prc, max_prc

    min_km, max_km, min_prc, max_prc = min(km), max(km), min(price), max(price)
    for i in range(len(km)):
        normalizeKm.append((float(km[i]) - min_km) / (max_km - min_km))
        normalizePrice.append((float(price[i]) - min_prc) / (max_prc - min_prc))
def estimatePrice(mileage, tempt0, tempt1):
    return ((tempt0 + (tempt1 * float(mileage))))
def meanSquareError():
    global km, price
    global tempt0, tempt1
    tmp_summ = 0.0

    for i in range(len(km)):
        tmp_diff = estimatePrice(km[i], tempt0, tempt1) - float(price[i])
        tmp_diff *= tmp_diff
        tmp_summ += tmp_diff

    return (tmp_summ / (len(km)))
def updateTeta0():
    global tempt0, tempt1
    global learning_rate, normalizeKm, normalizePrice
    tmp_summ = 0.0

    for i in range(len(normalizeKm)):
        tmp_summ += (estimatePrice(normalizeKm[i], tempt0, tempt1) - float(normalizePrice[i]))
    return (learning_rate * (tmp_summ / (len(normalizeKm))))
def updateTeta1():
    global tempt0, tempt1
    global learning_rate, normalizeKm, normalizePrice
    tmp_summ = 0.0

    for i in range(len(normalizeKm)):
        tmp_summ += (estimatePrice(normalizeKm[i], tempt0, tempt1) - float(normalizePrice[i])) * float(normalizeKm[i])

    return (learning_rate * (tmp_summ / len(normalizeKm)))
def modelPredict():
    global km, price
    global t0, t1, tempt0, tempt1
    global learning_rate, sharpness, meanErr
    global min_km, max_km, min_prc, max_prc

    normalizeData()
    meanErr = meanSquareError()
    sharpness = meanErr

    while sharpness > 0.000001 or sharpness < -0.000001:
        tempt0 -= updateTeta0()
        tempt1 -= updateTeta1()
        prevErr = meanErr
        meanErr = meanSquareError()
        sharpness = meanErr - prevErr

    t1 = (max_prc - min_prc) * tempt1 / (max_km - min_km)
    t0 = min_prc + ((max_prc - min_prc) * tempt0) + t1 * (-min_km)
def regressionPlot():
    global km, price
    global t0, t1, tempt0, tempt1
    global min_km, max_km, min_prc, max_prc

    plt.title('ft_linear_regression')
    plt.xlabel('Mileages')
    plt.ylabel('Prices')

    plt.plot(km, price, 'ro')    
    plt.plot([min_km, max_km], [estimatePrice(min_km, t0, t1), estimatePrice(max_km, t0, t1)])
    plt.axis([min_km - abs(max_km * 0.1), max_km + abs(max_km * 0.1), min_prc - abs(max_prc * 0.1), max_prc + abs(max_prc * 0.1)])

    plt.show()


# def prompt():
#     fileName = input("Dosya yolunu belirt: ")
#     print(open(fileName))

# prompt()
data = pd.read_csv('data.csv')

t0, t1 = 0.0, 0.0
learning_rate = 0.1
tempt0, tempt1 = 0.0, 0.0
meanErr, sharpness = 0.0, 0.0

km, price = data['km'], data['price']
normalizeKm, normalizePrice = [], []

modelPredict()
regressionPlot()

print(estimatePrice(240000, t0, t1))
