# imports
import cv2
import os

# check version
print(cv2.__version__)

# Directories
main_path = os.path.dirname(os.path.realpath(__file__))[:-4]

#add videos in videos_dir
#the extracted frames will be in extracted_frames_dir
source_path = './videos_dir/'
target_frames = './extracted_frames_dir/'

all_images = os.listdir(source_path)
for imagePath in all_images:

    vid = source_path + imagePath
    vidcap = cv2.VideoCapture(vid)
    length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    print ('Number of frames: ' + str(length))
    
    success, image = vidcap.read()



    count = 0
    success = True
    while success:
        cv2.imwrite(target_frames + imagePath[:-4] + "f%03d.jpg" % count, image)  # save frame as JPEG file
        success, image = vidcap.read()

        print 'Read a new frame: ', success
        count += 1
