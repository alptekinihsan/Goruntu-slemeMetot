import numpy as np
import random
import cv2

def sp_noise(image,prob):
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

image = cv2.imread('camereman.png',0)
cv2.imshow('Resim1',image);
noise_img = sp_noise(image,0.05)
cv2.imwrite('sp_noise.jpg', noise_img)
noise_img=cv2.imread('sp_noise.jpg')
cv2.imshow('Resim2',noise_img);
medyan  =  cv2.medianBlur ( noise_img , 5 )
cv2.imshow('Resim3',medyan)

cv2.waitKey(0);