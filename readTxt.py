import os
import re

def readTxtFunction(path,txtNum):
    f = open(path+"/det/det.txt")
    line = f.readline()
    result = []
    result.append([])
    indexOfPic = 1
    while line:
        dic = re.findall(r"\d+\.?\d*", line)
        if int(dic[0]) == indexOfPic:
            dicOfResult = [round(float(dic[2])),round(float(dic[3])),round(float(dic[4])),round(float(dic[5]))]
            result[indexOfPic-1].append(dicOfResult)
            line = f.readline()
        elif int(dic[0]) == indexOfPic+1:
            indexOfPic += 1
            result.append([])
            continue
    return result