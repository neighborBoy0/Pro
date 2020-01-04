import cv2 as cv
import readTxt

def getPicNum(picName):
    print(picName)
    numString = picName.split('.')[0]
    try:
        num = int(numString)
        return num
    except:
        return -1


def readPicFunction(path, path2, picName):
    txtNum = getPicNum(picName)
    if txtNum == -1:
        return -1
    else:
        img = cv.imread(path+path2+"/"+picName)
        rectangles = readTxt.readTxtFunction(path,txtNum)
        for rectangle in rectangles:
            image_rect = cv.rectangle(img,
                                      (rectangle[0], rectangle[1]),
                                      (rectangle[0]+rectangle[2], rectangle[1]+rectangle[3]),
                                      (0, 0, 255),
                                      2)

        cv.imwrite(path+"/result/"+picName,img)

        return 0