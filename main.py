import writeVideo
import extractFrame

# The directory of the folder where the video is located
path = "/Users/wangwei/Documents/我爱学习 学习爱我/Project/2DMOT2015/train/TUD-Stadtmitte"
listOfPic, numOfPic = extractFrame.readVideo(path, "video.mp4")    # Generate image arrays and position arrays
listOfRec = extractFrame.readTxt(path, numOfPic)     # The number of images in the incoming path and video

writeVideo.writeVideo(path, listOfPic, listOfRec, numOfPic)    #

