import cv2
import numpy as np
resim = cv2.imread("download.jpg")
cv2.imshow("Orjinal Resim", resim)

def GriYap(resim):
    en, boy, katman = np.shape(resim)
    yeniResim = np.zeros((en,boy,katman),dtype=np.uint8)

    for i in range(en):
        for j in range(boy):
            yeniResim[i:, j] = resim[i, j, 0] * 0.114 + resim[i, j, 1] * 0.587 + resim[i, j, 2] * 0.299

    cv2.imshow("Gri Resim", yeniResim)
GriYap(resim)
cv2.waitKey(0)