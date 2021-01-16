import cv2 as cv
import numpy as np
import cv2
import numpy as np
imgGri = cv2.imread("download.jpg")
cv2.imshow("orjinal resim",imgGri)
def GriYap(resim):
    en, boy, katman = np.shape(imgGri)
    yeniResim = np.zeros((en,boy,katman),dtype=np.uint8)

    for i in range(en):
        for j in range(boy):
            yeniResim[i:, j] = resim[i, j, 0] * 0.114 + resim[i, j, 1] * 0.587 + resim[i, j, 2] * 0.299
    cv2.imshow("Gri Resim", yeniResim)
    normalizedImg = np.zeros((800, 800))
    normalizedImg = cv.normalize(yeniResim, normalizedImg, 0, 50, cv.NORM_MINMAX)
    cv2.imshow('Normalize', normalizedImg)
GriYap(imgGri)
cv.waitKey(0)
cv.destroyAllWindows()