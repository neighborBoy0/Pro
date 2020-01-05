import cv2
import numpy
import os

"""
* objective: crop a picture into multiple rectangles and save these rectangles
* enter: pic - a picture; 
         recOfPic - all of rectangles in the video; 
         i - the i th picture;
         path - working directory;
         widthOfPic - length of picture/video
         heightOfPic - height of picture/video
* return: result - list of all of information of rectangles in the i th picture
"""
def slicingFunction(pic, recOfPic, i, path, widthOfPic, heightOfPic):
    result = []
    z = 1
    for rec in recOfPic:

        x = rec[0]  # x: horizontal ordinate of upper-left corner of rectangle
        y = rec[1]  # y: vertical coordinates of upper-left corner of rectangle
        width = rec[2]   # width of rectangle
        heigth = rec[3]  # height of rectangle

        # (x2, y2): Coordinates of the bottom right corner of the rectangle
        # y2: vertical coordinates of the bottom right corner of the rectangle
        if y + heigth >= widthOfPic:
            y2 = widthOfPic-1
        else:
            y2 = y + heigth

        # x2: horizontal ordinate of the bottom right corner of the rectangle
        if x + width >= heightOfPic:
            x2 = heightOfPic-1
        else:
            x2 = x + width

        # crop/cut the picture according to the rectangle
        # y:y2 = Height range of the rectangle
        # x:x2 = Width range of the rectangle
        picTemp = pic[y:y2, x:x2]

        picName = str(i) + "-" + str(z)
        z += 1

        # save these rectangle
        try:
            if not os.path.exists(path + '/result'):
                os.makedirs(path + '/result')
        except OSError:
            print('Error: Creating directory of result !')
        cv2.imwrite(path + "/result/" + picName + ".jpg", picTemp)

        # for every rectangle, we should calculate:
        # the first element in resultTemp: the coordinate of the middle of the bottom edge
        # the second element in resultTemp: the length and height of the rectangle,
        # the third element in resultTemp: the average of RGB
        resultTemp = [[rec[1] + (rec[3] / 2), rec[0] + rec[2]],
                      [rec[3], rec[2]],
                      numpy.mean(picTemp, 0).mean(0)]
        result.append(resultTemp)

    return result