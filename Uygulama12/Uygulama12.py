import numpy as np
import cv2
from matplotlib import pyplot as plt
resim=cv2.imread("image.PNG")
plt.imshow(resim)
plt.show()
def sobelOperator(img):
    toplam = np.copy(img)
    size = toplam.shape
    for i in range(1, size[0] - 1):
        for j in range(1, size[1] - 1):
            """
            Gelen Resime Göre 
                  _               _                   _                _
                 |                 |                 |                  |
                 | 1.0   0.0  -1.0 |                 |  1.0   2.0   1.0 |
            Gx = | 2.0   0.0  -2.0 |      ve    Gy = |  0.0   0.0   0.0 |       Oluşturma
                 | 1.0   0.0  -1.0 |                 | -1.0  -2.0  -1.0 |
                 |_               _|                 |_                _|
            """
            gx = (img[i - 1][j - 1] + 2*img[i][j - 1] + img[i + 1][j - 1]) - (img[i - 1][j + 1] + 2*img[i][j + 1] + img[i + 1][j + 1])
            gy = (img[i - 1][j - 1] + 2*img[i - 1][j] + img[i - 1][j + 1]) - (img[i + 1][j - 1] + 2*img[i + 1][j] + img[i + 1][j + 1])
            toplam[i][j] = min(255, np.sqrt(gx**2 + gy**2))
    return toplam
    pass
img = cv2.cvtColor(cv2.imread("image.PNG"), cv2.COLOR_BGR2GRAY)
plt.imshow(img)
plt.show()
img = sobelOperator(img)
img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
plt.imshow(img)
plt.show()