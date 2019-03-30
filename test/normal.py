import cv2 as cv
import numpy as np

def normal(img):
    img_s = img[:, :, 0] + img[:, :, 1] + img[:, :, 2]
    mean = np.mean(img_s)
    img_n = img_s - mean
    return img_n 

def normal2(img):
    for i in range(3):
        img[:, :, i] = img[:, :, i] - np.mean(img[:, :, i])
    return img

def normal3(img):
    img = cv.cvtColor(img, cv.CV_BGR2GRAY)
    gray_lap = cv.Laplacian(img, cv.CV_16S, ksize= 3)
    dst = cv.convertScaleAbs(gray_lap)
    return dst

def get_similarity(img_1, img_2, func):
    img_1 = func(img_1)
    img_2 = func(img_2)

    img_dis = np.absolute(img_1, img_2)
    similarity = int(np.sum(img_dis))
    return similarity