import cv2
import numpy as np
resim = cv2.imread("camereman.png")
cv2.imshow("Orjinal Resim", resim)
x=int(input("satır  "));
y=int(input("sütun  "));
en, boy, katman = np.shape(resim)
yeniResim = np.zeros((en, boy, katman), dtype=np.uint8)

for i in range(90):
    for j in range(90):
        yeniResim[i, j]= resim[x+i, y+j];
cv2.imshow("yeniresim", yeniResim)

cv2.waitKey(0)