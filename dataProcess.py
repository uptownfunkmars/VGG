import os
import random
import numpy as np
import cv2


def dataAugmentation(img):
    # 旋转flip
    # 平移
    # 缩放
    # 滤波 考虑
    num = np.random.random()
    if num < 0.2:
        img = imgRotate(img, 45)
    elif num < 0.4:
        img = imgRotate(img, 90)
    elif num < 0.6:
        img = imgRotate(img, 135)
    elif num < 0.8:
        img = imgRotate(img, 270)

    return img


def imgFlip(img):
    if np.random.random() < 0.25:
        img = cv2.flip(img, 0)
    elif np.random.random() > 0.85:
        img = cv2.flip(img, 1)

    return img


def imgRotate(img, angle):
    shape = img.shape

    h = shape[0]
    w = shape[1]
    m_rotate = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1)

    img = cv2.warpAffine(img, m_rotate, (w, h))

    return img


def colorJitter(img):
    pass


def dataGen(positive_path, negative_path, batch_size, shuffle=True):
    x = []
    y = []

    positiveFileName = os.listdir(positive_path)
    negativeFileName = os.listdir(negative_path)

    for pfn in positiveFileName:
        absPth = positive_path + "/" + pfn

        # img = cv2.imread(absPth)
        # img = dataAugmentation(img)

        x.append(absPth)
        y.append(1)

    for nfn in negativeFileName:
        absPth = negative_path + "/" + nfn

        # img = cv2.imread(absPth)
        # img = dataAugmentation(img)

        x.append(absPth)
        y.append(0) 

    assert len(x) == len(y), "length a and length b not equal!"

    idx = [i for i in range(len(x))]
    random.shuffle(idx)

    base = 0
    for i in range((len(x) // batch_size)):
        inputs = []
        inputs_name = []
        labels = []        

        inputs_idx = idx[base:base + batch_size]
        
        for j in inputs_idx:
            inputs_name.append(x[j])
            labels.append(y[j])
        
 
        for j in inputs_name:
            img = cv2.imread(j)
            img = dataAugmentation(img)
            inputs.append(img)
        
        base += batch_size
        
        yield np.array(inputs), np.array(labels)


'''
def dataGen(positive_path, negative_path, batch_size, shuffle=True):
    x = []
    y = []

    positiveFileName = os.listdir(positive_path)
    negativeFileName = os.listdir(negative_path)
    
    print("Reading positive samples...")
    for pfn in positiveFileName:
        absPth = positive_path + "/" + pfn
        
        img = cv2.imread(absPth)
        img = dataAugmentation(img)

        x.append(img)
        y.append(0)
    print("Done")


    print("Reading negative samples...")
    for nfn in negativeFileName:
        absPth = negative_path + "/" + nfn

        img = cv2.imread(absPth)
        img = dataAugmentation(img)

        x.append(img)
        y.append(1)
    print("Done")
    
    print("Shuffling...")    
    idx = [i for i in range(len(x))]
    random.shuffle(idx)

    base = 0
    for i in range((len(x) / batch_size)):
        inputs = x[base:base + batch_size]
        labels = y[base:base + batch_size]

        base += batch_size

        yield inputs, labels
'''
