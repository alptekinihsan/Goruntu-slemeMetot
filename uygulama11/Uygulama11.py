import cv2
import numpy as np

imgGri = cv2.imread("download.jpg")
cv2.imshow("Resim",imgGri)
def GriYap(resim):
    en, boy, katman = np.shape(imgGri)
    yeniResim = np.zeros((en, boy, katman), dtype=np.uint8)

    for i in range(en):
        for j in range(boy):
            yeniResim[i:, j] = resim[i, j, 0] * 0.114 + resim[i, j, 1] * 0.587 + resim[i, j, 2] * 0.299
    cv2.imshow("Gri Resim", yeniResim)
    gaus = cv2.GaussianBlur(yeniResim, (5, 5), 0)
    cv2.imshow("Gaussian",gaus)
GriYap(imgGri)



cv2.waitKey(0)


