import cv2
import numpy as np
resim = cv2.imread("download.jpg")
cv2.imshow("Orjinal Resim", resim)
x=0.5;
y=2;
en, boy, katman = np.shape(resim)
yeniresim = np.zeros((en, boy, katman), dtype=np.uint8)
yeniresim2 = np.zeros((en, boy, katman), dtype=np.uint8)
for i in range(en):
    for j in range(boy):
        yeniresim[i, j] = x*resim[i, j];
        yeniresim2[i,j] = y*resim[i, j];
cv2.imshow("YeniResim", yeniresim)
cv2.imshow("YeniResim", yeniresim2)



cv2.waitKey(0)