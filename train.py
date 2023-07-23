import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from dataReader import getData

# Tahmini fiyatı hesaplamak için fonksiyon
def tahmini_fiyat(kilometre, theta0, theta1):
    return theta0 + (theta1 * kilometre)

# Doğrusal regresyonu yapacak ve theta0 ve theta1 değerlerini güncelleyecek fonksiyon
def dogrusal_regresyon_egitimi(kilometre, fiyat, theta0, theta1, ogrenme_orani, iterasyon_sayisi):
    m = len(kilometre)
    for i in range(iterasyon_sayisi):
        tmp_theta0 = 0
        tmp_theta1 = 0
        for i in range(m):
            tmp_theta0 += tahmini_fiyat(kilometre[i], theta0, theta1) - fiyat[i]
            tmp_theta1 += (tahmini_fiyat(kilometre[i], theta0, theta1) - fiyat[i]) * kilometre[i]
        
        tmp_theta0 *= ogrenme_orani / m
        tmp_theta1 *= ogrenme_orani / m
        
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1

        print(theta0, theta1)
        
    return theta0, theta1

if __name__ == "__main__":
    kilometre, fiyat = getData('data.csv')

    theta0 = 0
    theta1 = 0

    ogrenme_orani = 0.001
    iterasyon_sayisi = 10

    theta0, theta1 = dogrusal_regresyon_egitimi(kilometre, fiyat, theta0, theta1, ogrenme_orani, iterasyon_sayisi)

    with open("theta_degerleri.txt", "w") as dosya:
        dosya.write(f"{theta0} {theta1}")

    print("Eğitim tamamlandı. Eğitilmiş theta0 ve theta1 değerleri kaydedildi.")
