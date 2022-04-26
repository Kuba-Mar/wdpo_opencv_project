import cv2
import numpy as np
import sys


def nothing(value):
    print(f'Trackbar reporting for duty with value: {value}')
    pass

def banana_nubmer(img):
    scale_percent = 20  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)

    hLb = 20
    hHb = 50
    vLb = 130
    vHb = 255
    sLb = 108
    sHb = 250

    lower_b = np.array([hLb, sLb, vLb])
    upper_b = np.array([hHb, sHb, vHb])

    mask_banana = cv2.inRange(hsv, lower_b, upper_b)
    kernel = np.ones((7, 7), np.uint8)

    closing_banana = cv2.morphologyEx(mask_banana, cv2.MORPH_CLOSE, kernel)
    dilation_banana = cv2.dilate(closing_banana, kernel, iterations=1)
    contours_banana, hierarchy = cv2.findContours(dilation_banana, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    banana = 0
    for cnt in contours_banana:
        area = cv2.contourArea(cnt)
        value = int(area)
        if (value > 10000):
            banana += 1
    return banana

def orange_number(img):
    scale_percent = 20  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)

    hL = 66
    hH = 92
    vL = 25
    vH = 92
    sL = 75
    sH = 192

    hL1 = 0
    hH1 = 18
    vL1 = 130
    vH1 = 255
    sL1 = 220
    sH1 = 250

    lower = np.array([hL, sL, vL])
    upper = np.array([hH, sH, vH])

    lower1 = np.array([hL1, sL1, vL1])
    upper1 = np.array([hH1, sH1, vH1])

    mask1 = cv2.inRange(hsv, lower, upper)
    mask2 = cv2.inRange(hsv, lower1, upper1)

    mask = mask1 + mask2
    kernel = np.ones((7, 7), np.uint8)

    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    contours, hierarchy1 = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    orange = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        value = int(area)
        if (value > 5000):
            orange += 1
    return orange


def apple_number(img):

    scale_percent = 20  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
    hL = 0
    hH = 14
    vL = 36
    vH = 255
    sL = 36
    sH = 220

    hL1 = 70
    hH1 = 179
    vL1 = 36
    vH1 = 255
    sL1 = 36
    sH1 = 255

    lower = np.array([hL, sL, vL])
    upper = np.array([hH, sH, vH])

    lower1 = np.array([hL1, sL1, vL1])
    upper1 = np.array([hH1, sH1, vH1])

    mask1 = cv2.inRange(hsv, lower, upper)
    mask2 = cv2.inRange(hsv, lower1, upper1)

    mask = mask1 + mask2
    kernel = np.ones((7,7), np.uint8)

    dilation = cv2.dilate(mask, kernel, iterations=1)
    closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)

    contours, hierarchy1 = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    apple = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        value = int(area)
        if (value > 9000):
            apple += 1
    return apple



if __name__ == "__main__":
    img = cv2.imread('/Users/kuba/PycharmProjects/projekt/data/02.jpg', cv2.IMREAD_UNCHANGED)
    print("Liczba bananow: " + str(banana_nubmer(img)))
    print("Liczba pomaranczy: " + str(orange_number(img)))
    print("Liczba jablek: " + str(apple_number(img)))