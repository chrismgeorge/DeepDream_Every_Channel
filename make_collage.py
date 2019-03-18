import numpy as np
import cv2
import os

def getImages():
    images = np.load('./numpy_images.npy', 'r')
    i = 0
    test_dir = './test_images/'
    for image in images:
        npimg = image
        npimg = npimg-np.amin(npimg)
        npimg = npimg/np.amax(npimg)
        npimg = np.transpose(npimg, (1,2,0))
        npimg *= 255
        image = np.asarray(npimg, dtype='uint8')
        name = '{num:0{width}}'.format(num=i, width=6)+'.png'
        cv2.imwrite('%s%s' % (test_dir,name), image)
        i += 1

def makeMegaCollage():
    directory_path = "./test_images/"

    getImages()

    # contains excess files, so don't use length as check if # of pics
    files = os.listdir(directory_path)
    nFiles = len(files)
    print(nFiles)
    collage_photos = 60
    rows = 24
    cols = 24
    img = np.zeros([64*cols, 64*rows, 3])

    a = set()

    curRow = 0

    curCol = 0
    for filename in os.listdir(directory_path):
        file_path = directory_path+filename
        if (".png" in file_path):

            pic = cv2.imread(file_path, cv2.IMREAD_COLOR)

            dx = (curCol)*64
            dy = (curRow)*64

            for row in range(0, len(pic)):
                for col in range(0, len(pic[0])):

                    img[dx+row, dy+col, 0] = pic[row, col, 0]
                    img[dx+row, dy+col, 1] = pic[row, col, 1]
                    img[dx+row, dy+col, 2] = pic[row, col, 2]

            curCol += 1
            if (curCol == 24):
                curCol = 0
                curRow += 1
            print(curCol)

        print("Finished... ", str(curRow)+"/"+str(nFiles))

    cv2.imwrite('the_meg.jpg', img)

makeMegaCollage()
