from PIL import Image

def imageToList(imagePath):
    image = Image.open(imagePath)
    imageSize = image.size
    pixels = list(image.getdata())
    return pixels,imageSize

def pictureMapper(imagePath="cat.jpg"):
    imageData =imageToList(imagePath)
    imageSize = imageData[1]
    mappedPicture = []

    for lineCounter in range(imageSize[0]):
        mappedPicture.append(imageData[0][(imageSize[0] * lineCounter) : (imageSize[0] * lineCounter + 640)])

    return mappedPicture,imageSize

def turnRight180Degree(imagePath,saveName):
    mappedPicList = pictureMapper(imagePath)
    picData = mappedPicList[0]
    picSize = int(mappedPicList[1][1]-1)
    tmp = []
    pictureResult = []
    for row in picData:
        tmp.insert(0,row)

    for i in range(mappedPicList[1][1]-1):
        pictureResult.extend(tmp[i])


    new_image = Image.new(mode="RGB",size=((picSize + 1) , (picSize + 1)))
    new_image.putdata(pictureResult)
    new_image.save("{0}.jpg".format(saveName))
    return "{0}.jpg".format(saveName)

def turnLeft90Degree(imagePath,saveName):
    mappedPicList = pictureMapper(imagePath)
    picData = mappedPicList[0]
    picHeight = int(mappedPicList[1][1])
    picWidth = int(mappedPicList[1][0])
    tmp = []
    pictureResult = []

    for columnIndex in range(picWidth):
        tmp.append([])
        for rowIndex in range(picHeight):
            tmp[columnIndex].append(picData[rowIndex][columnIndex])

    for i in range(picHeight - 1):
        pictureResult.extend(tmp[i])

    new_image = Image.new(mode="RGB", size=((picWidth), (picHeight)))
    new_image.putdata(pictureResult)
    new_image.save("{0}.jpg".format(saveName))
    return "{0}.jpg".format(saveName)

def  turnRight90Degree(imagePath,saveName):
    image = turnRight180Degree(imagePath,saveName)
    image = turnLeft90Degree(image,saveName)
    print("image is saved: {}".format(image))

# A funny mistake
# def turnRight90Degree(imagePath):
#     mappedPicList = pictureMapper(imagePath)
#     picData = mappedPicList[0]
#     picSize = int(mappedPicList[1][1] - 1)
#     tmp = []
#     pictureResult = []
#
#     for columnIndex in range(picSize):
#         tmp.append([])
#         for pixelInRow in range(picSize):
#             tmp[columnIndex].insert(0,picData[columnIndex][pixelInRow])
#
#     for i in range(mappedPicList[1][1] - 1):
#         pictureResult.extend(tmp[i])
#
#     new_image = Image.new(mode="RGB", size=((picSize + 1), (picSize + 1)))
#     new_image.putdata(pictureResult)
#     new_image.save("new.jpg")

if __name__ == '__main__':
    turnRight90Degree("cat.jpg","hello")




