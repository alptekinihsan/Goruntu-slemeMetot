import cv2
import numpy as np
resim = cv2.imread("download.png")
cv2.imshow("Orjinal Resim", resim)

def TersÇevirme(resim):
    en,boy,katman=np.shape(resim)
    yeniresim = np.ones((en, boy, katman))
    for i in range (en-1):
        for j in range (boy-1):
            yeniresim[i+1:, j+1]=resim[i+1,boy-j,2]
    cv2.imshow("TersAlma",yeniresim)

TersÇevirme(resim)
cv2.waitKey(0)