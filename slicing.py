import cv2
import numpy

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
        # rec[1]+rec[3] is the vertical coordinates of left of rectangle +
        # vertical coordinates of right of rectangle
        if rec[1] + rec[3] >= widthOfPic:
            right = widthOfPic-1
        else:
            right = rec[1] + rec[3]

        # rec[0]+rec[2] is the horizontal ordinate of the top of rectangle +
        # horizontal ordinate of the bottom of rectangle
        if rec[0] + rec[2] >= heightOfPic:
            down = heightOfPic-1
        else:
            down = rec[0] + rec[2]

        picTemp = pic[rec[1]:right, rec[0]:down]   # crop the picture according to the rectangle

        picName = str(i) + "-" + str(z)
        z += 1
        cv2.imwrite(path + "/result/" + picName + ".jpg", picTemp)   # save these rectangle

        # for every rectangle, we should calculate the coordinate of the middle of the bottom edge
        # (the first element in resultTemp), the length and height of the rectangle(the second element in resultTemp),
        # the average of RGB(the third element in resultTemp)
        resultTemp = [[rec[1] + (rec[3] / 2), rec[0] + rec[2]], [rec[3], rec[2]], numpy.mean(picTemp,0).mean(0)]
        result.append(resultTemp)

    return result