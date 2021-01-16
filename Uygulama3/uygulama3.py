import cv2
import numpy as np
resim = cv2.imread("download.jpg")
cv2.imshow("Orjinal Resim", resim)

GriResim = resim[:, :, 0]
cv2.imshow("Gri Resim", GriResim)

def siyahBeyazYap(resim, esik):
    en, boy, katman = np.shape(resim)

    yeniResim = np.ones((en, boy, katman))

    for i in range(en):
        for j in range(boy):
            if (resim[i, j, 0] > esik):
                yeniResim[i, j] = 1
            else:
                yeniResim[i, j] = 0
    cv2.imshow("Siyah Beyaz", yeniResim)
siyahBeyazYap(resim, 100)
cv2.waitKey(0)