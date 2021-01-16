import cv2
import numpy as np
resim = cv2.imread("download.jpg")
cv2.imshow("Orjinal Resim", resim)

def Transpoz(resim):
    en,boy,katman=np.shape(resim)
    yeniresim = np.ones((en, boy, katman))
    yeniresintrans=np.transpose(yeniresim)
    for i in range (en-1):
        for j in range (boy-1):
            yeniresintrans[i+1:, j+1]=resim[i+1,boy-j]
    cv2.imshow("Transpoz",yeniresim)

Transpoz(resim)
cv2.waitKey(0)