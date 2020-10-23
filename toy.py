import cv2 as cv
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--arg1', type=int, default=1, help='help something')
parser.add_argument('--arg2', type=int, default=2, help='help something')
parser.add_argument('--arg3', type=int, default=3, help='help something')

FLAGS = parser.parse_args()

print(FLAGS.arg1)


def imgRotate(img, angle):
    shape = img.shape

    h = shape[0]
    w = shape[1]
    m_rotate = cv.getRotationMatrix2D((w // 2, h // 2), angle, 1)

    img = cv.warpAffine(img, m_rotate, (w, h))

    return img


img = cv.imread("timg.jpg")
img = cv.resize(img, (480, 640))
print("h, w, c")
print(img.shape)

img = imgRotate(img, 45)

print(img.shape)

cv.namedWindow('123')
cv.imshow('123', img)
cv.waitKey()
cv.destroyWindow('123')



