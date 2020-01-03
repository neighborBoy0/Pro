import writeVideo
import extractFrame

# The directory of the folder where the video is located
path = "/Users/wangwei/Documents/我爱学习 学习爱我/Project/2DMOT2015/train/TUD-Stadtmitte"

# Generate image arrays and position arrays
listOfPic, numOfPic = extractFrame.readVideo(path, "video.mp4")

# The number of images in the incoming path and video
listOfRec = extractFrame.readTxt(path, numOfPic)

'''
1. Slice the rectangles
2. Draw graphs
3. Match the graphs
4. Product a new video
'''
writeVideo.writeVideo(path, listOfPic, listOfRec, numOfPic)

