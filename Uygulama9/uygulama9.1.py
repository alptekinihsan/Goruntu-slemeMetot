import cv2
import numpy as np
import matplotlib.pyplot as plt
imgGri = cv2.imread("download.jpg")
def GriYap(resim):
    en, boy, katman = np.shape(imgGri)
    yeniResim = np.zeros((en,boy,katman),dtype=np.uint8)

    for i in range(en):
        for j in range(boy):
            yeniResim[i:, j] = resim[i, j, 0] * 0.114 + resim[i, j, 1] * 0.587 + resim[i, j, 2] * 0.299

    cv2.imshow("Gri Resim", yeniResim)
GriYap(imgGri)
en, boy,katman = np.shape(imgGri)
hist = np.zeros((256,1), dtype=np.uint8)

for i in range(en):
    for j in range(boy):
        hist[imgGri[i, j]+1] = hist[imgGri[i, j]+1]+1

plt.plot(hist)
plt.show()

cv2.waitKey(0)