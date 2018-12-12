#!/usr/bin/env python
import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt

def img__test():
    img__src = cv2.imread('D:\\PycharmProjects\\Project_TANDAV(JEAL_JORSTA)\\res\\smpl2.jpg', cv2.IMREAD_ANYCOLOR)

    plt.imshow(img__src, cmap='viridis', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])
    plt.plot([200, 300, 400], [100, 200, 300], 'c', linewidth=5)
    plt.show( )

def img__display():
    img__src = cv2.imread('D:\\PycharmProjects\\Project_TANDAV(JEAL_JORSTA)\\res\\smpl2.jpg')       #load image into this function
    (h, w, d) = img__src.shape
    print('width = {}, height = {}, depth = {}'.format(w, h, d))
    cv2.imshow('Image', img__src)
    cv2.waitKey(0)


def RGB__colorCode__find():
    img__src = cv2.imread('D:\\PycharmProjects\\Project_TANDAV(JEAL_JORSTA)\\res\\smpl2.jpg')
    (h, w, d) = img__src.shape
    (B, G, R) = img__src[100, 50]
    print('R = {}, G = {}, B = {}'.format(R, G, B))
    cv2.imshow('Image', img__src)
    cv2.waitKey(0)

def RIO__declear():         #Region of interest == ROI
    img__src = cv2.imread('D:\\PycharmProjects\\Project_TANDAV(JEAL_JORSTA)\\res\\smpl2.jpg')
    (h, w, d) = img__src.shape
    ROI = img__src[60:120, 320:420]
    cv2.imshow('ROI', ROI)
    cv2.waitKey(0)

def face_dtect():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    face_cascade.load('D:\\PycharmProjects\\Project_TANDAV(JEAL_JORSTA)\\dep_pkgs\\haarcascades\\haarcascade_frontalface_default.xml')
    eye_cascade.load('D:\\PycharmProjects\\Project_TANDAV(JEAL_JORSTA)\\dep_pkgs\\haarcascades\\haarcascade_eye.xml')

    img = cv2.imread('D:\\PycharmProjects\\Project_TANDAV(JEAL_JORSTA)\\res\\smpl2.jpg')
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(grey_img, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x, y), (x+w, y+h), (255, 0, 0),2)
        ROI_grey = grey_img[y:y+h, x:x+w]
        ROI_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(ROI_grey)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(ROI_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('img', img)
    cv2.waitKey(0)

if __name__ == '__main__':
    img__test()
    img__display()
    RGB__colorCode__find()
    RIO__declear()
    face_dtect()
