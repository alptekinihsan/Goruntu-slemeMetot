import cv2
import numpy as np
import matplotlib.pyplot as plt
resim = cv2.imread("images.jpg")
cv2.imshow("Orjinal Resim", resim)

en, boy,katman = np.shape(resim)
hist = np.zeros((256,1), dtype=np.uint8)

for i in range(en):
    for j in range(boy):
        hist[resim[i, j]+1] = hist[resim[i, j]+1]+1

plt.plot(hist)
plt.show()

cv2.waitKey(0)