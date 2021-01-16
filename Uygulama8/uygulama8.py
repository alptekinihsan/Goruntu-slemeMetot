import cv2
import numpy as np
resim = cv2.imread("download.jpg")
cv2.imshow("Orjinal Resim", resim)

en, boy, katman = np.shape(resim)
yeniresim = np.zeros((en, boy, katman), dtype=np.uint8)

for i in range(en):
    for j in range(boy):
        yeniresim[i, j] = 255-resim[i, j];

cv2.imshow("YeniResim", yeniresim)


cv2.waitKey(0)