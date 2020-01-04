import cv2
import os
import numpy
import re


"""
* objective: read video
* input: videoPath - directory of video; videoName - name of video
* output: listFrame - list of pictures; currentframe - the number of pictures
"""
def readVideo(videoPath, videoName):

    # Read the video from specified path
    video = videoPath + "/" +videoName
    vidcap = cv2.VideoCapture(video)

    try:
        # creating a folder named img
        if not os.path.exists(videoPath + '/img'):
            os.makedirs(videoPath + '/img')

    # if not created then raise error
    except OSError:
        print('Error: Creating directory of video !')

    # frame begin of number 1
    currentframe = 0

    # create a list to stock the frames
    listFrame = []  # vide list

    while(True):
        # ret: return if success
        # frame: return a frame
        ret, frame = vidcap.read()

        if ret:
            # if video is still left continue creating images
            name = videoPath + '/img/' + str(currentframe) + '.jpg'
            print('Creating...' + name)

            # writing the extracted images
            # name: the path to save this frame
            # frame: this frame image
            # cv.imwrite(name, frame)

            # add(append) this frame in the list of frame
            frameOnNumpy = numpy.array(frame)
            listFrame.append(frameOnNumpy)

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break

    print('end')

    # Release all space and windows once done
    vidcap.release()
    cv2.destroyAllWindows()
    return listFrame, currentframe

"""
* objective: read .txt file
* input: path - directory of video; txtNum - the number of pictures
* output: result - a three-dimensional list; 
            the first dimensional - pictures
            the second dimensional - rectangles in the picture
            the third dimensional - the detail of the rectangle
"""
def readTxt(path,txtNum):

    f = open(path+"/det/det.txt")    # open the .txt file
    line = f.readline()
    result = []
    result.append([])
    indexOfPic = 1

    while line:
        dic = re.findall(r"\d+\.?\d*", line)    # find all of figures in this line, 'dic' is a list;
        # dic[0] points to the picture
        # dic[1]
        # dic[2] is the horizontal ordinate of the top left corner of the rectangle
        # dic[3] is the vertical coordinates of the top left corner of the rectangle
        # dic[4] is the length of the rectangle
        # dic[5] is the height of the rectangle

        if int(dic[0]) == indexOfPic:   # when this line is a rectangle in the 'indexOfPic'th picture
            dicOfResult = [round(float(dic[2])),
                           round(float(dic[3])),
                           round(float(dic[4])),
                           round(float(dic[5]))]
            result[indexOfPic-1].append(dicOfResult)
            line = f.readline()

        elif int(dic[0]) == indexOfPic+1:   # when not
            indexOfPic += 1
            result.append([])
            continue

    return result