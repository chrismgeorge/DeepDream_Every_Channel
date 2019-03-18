import numpy as np
import cv2
import os
from PIL import ImageEnhance
from PIL import Image

def main():
    # Guassian Kernel
    kernel = (-1/256)*np.array([[1,4,6,4,1], [4,16,24,16,4], [6,24,-476,24,6], [4,16,24,16,4], [1,4,6,4,1]])

    # Directory and Channels
    directory = './processed_images/'
    channels = os.listdir(directory)

    for channel in channels:
        if ('pre' in channel):
            files = os.listdir(directory+channel)
            print(channel)
            for image in files:
                if ('.jpg' in image):
                    filePath = directory+channel+"/"+image
                    # Saturate the image
                    img = Image.open(filePath)
                    converter = ImageEnhance.Color(img)
                    saturatedImage = converter.enhance(2)
                    saturatedImage = np.array(saturatedImage)

                    # Sharpen the image
                    sharpenedImg = cv2.filter2D(saturatedImage, -1, kernel)
                    cv2.imwrite(filePath, sharpenedImg)

    print('Done!')

main()
