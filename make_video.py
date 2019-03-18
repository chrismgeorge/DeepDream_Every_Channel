import numpy as np
import cv2
import os

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

directory = './test_images/'
images = os.listdir(directory)

video_dir = './video/'
video_name = video_dir+'video4.mp4'
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
video = cv2.VideoWriter(video_name, fourcc, 24.0, (64, 64))

frameCount = 0
for i in range(len(images)):
    name = directory+'{num:0{width}}'.format(num=frameCount, width=6)+'.png'
    if (os.path.isfile(name)):
        video.write(cv2.imread(name))
        frameCount += 1
        if (frameCount % 100 == 0):
            print('Frame: ', frameCount)
        os.remove(name)

cv2.destroyAllWindows()
video.release()
