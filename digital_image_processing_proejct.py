

#I.png görseli RGB bir görüntüdür. Üzerinde koyu tonda hücreler ve onların etrafını saran beyaz renkte sitoplazma bulunmaktadır.
#Görüntüdeki sitoplazmanın (beyaz tonların) tüm görsele olan oranını bulunuz.

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imread = cv.imread
fig = plt.figure
subplot = plt.subplot
imshow = plt.imshow
# Görüntünün yüklenmesi
I = cv.imread('I.png')

# OpenCV görüntüyü BGR formatında okuduğu için onu RGB formatına dönüştürme
I_rgb = cv.cvtColor(I, cv.COLOR_BGR2RGB)

#Sitoplazmayı temsil eden beyaz tonlar için threshold belirleme. Pikselin beyaz ton sayılması için 185'ten büyük değerde olmalıdır.
#(Burada sitoplazma tam beyaz olmadığı için esnek bir sınır seçilmiştir.)
threshold = 200

#Threshold'dan büyük olan piksellerin belirlenip daha sonra sayısının elde edilmesi
I_sitoplazma = np.all(I_rgb > threshold, axis=2)
sitoplazma_pixels = np.sum(I_sitoplazma)

#Görüntüdeki toplam piksel sayısının bulunması
total_pixels = I_rgb.shape[0] * I_rgb.shape[1]

#Threshold'dan büyük piksel sayısının tüm piksel sayısına oranının bulunması ve yazdırılması
ratio = sitoplazma_pixels / total_pixels
print(f"Beyaz tonların oranı: {ratio:.2%}")

#Orijinal görüntünün ve threshold uygulanmış görüntünün gösterilmesi
fig()

#Orijinal Görüntü
subplot(1, 2, 1), imshow(I_rgb)

#Threshold uygulanmış görüntü
subplot(1, 2, 2), imshow(I_sitoplazma, cmap='gray')

