# imports
import cv2
import os

# check version
print(cv2.__version__)

# Directories
main_path = os.path.dirname(os.path.realpath(__file__))[:-4]
run = "fights/"
walk = "noFights/"
# sources
data_path = main_path + "Dataset/"
run_path = data_path + run
walk_path = data_path + walk
test_path = data_path + 'test/'
# destinations
run_frames = main_path + "Frames/" + run
walk_frames = main_path + "Frames/" + walk
test_frames = main_path + "Frames/" + "test/"
print(run_frames, walk_frames)

source_path = './test_vid/'
target_frames = './Test_Folder/'

all_images = os.listdir(source_path)
for imagePath in all_images:

    vid = source_path + imagePath
    # print(vid)
    vidcap = cv2.VideoCapture(vid)
    success, image = vidcap.read()
    count = 0
    success = True
    while success:
        cv2.imwrite(target_frames + imagePath[:-4] + "f%03d.jpg" % count, image)  # save frame as JPEG file
        success, image = vidcap.read()

        print 'Read a new frame: ', success
        count += 1
