import os
import shutil
import cv2


originalannotations = "FullIJCNN2013/gt.txt"
originalimages = "FullIJCNN2013/"
destimages = "GT_SPLITTED"
os.mkdir(destimages)

def annotationcalc(source, dest, splitted, signalcode, classcount1):
    

    img = cv2.imread(source,0)
    height, width = img.shape[:2]

    print(height, width)

    x1 = int(splitted[1])
    x2 = int(splitted[3])

    y1 = int(splitted[2])
    y2 = int(splitted[4])

    absheight = (y2 - y1)/height
    abswidth = (x2 - x1)/width

    centerx = (x2 + x1)/2
    centery = (y2 + y1)/2

    absx = centerx/width
    absy = centery/height


    class_, classcount1 = classcalculation(signalcode, classcount1)
    f = open(dest.replace(".ppm",".txt"),"a")
    f.write(str(class_) + " " + str(absx) + " " + str(absy) + " " + str(abswidth) + " " + str(absheight) + "\n")

    return classcount1


def mainprog():
    f = open(originalannotations)
    lines = f.readlines()
    classcount1 = [0,0,0]
    listimages = []

    for j in range(2):
        for i,line in enumerate(lines):
            if i == 0:
                continue

            splitted = line.split(";")
            signalcode = splitted[5].strip()
            filename = splitted[0].strip()
        

            if (int(signalcode) >= 0 and int(signalcode)<=8) and j == 0:
            
                source = originalimages + filename
                dest = destimages + "/" + filename
                image = cv2.imread(source)
                cv2.imwrite(dest.replace(".ppm",".jpg"), image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
                classcount1 = annotationcalc(source, dest, splitted, signalcode, classcount1)
            
                listimages.append(filename)

            elif ((filename in listimages) and ((int(signalcode) >= 19 and int(signalcode) <= 31) or (int(signalcode) >= 33 and int(signalcode) <= 40)) and j == 1):
                source = originalimages + filename
                dest = destimages + "/" + filename
            
                image = cv2.imread(source)
                cv2.imwrite(dest.replace(".ppm",".jpg"), image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
                classcount1 = annotationcalc(source, dest, splitted, signalcode,classcount1)

    print(classcount1)

def classcalculation(signalcode, classcount1):
    if int(signalcode) >= 0 and int(signalcode)<=8:
        class_ = 1
        classcount1[0] = classcount1[0] + 1
    
    if int(signalcode) >= 19 and int(signalcode) <= 31:
        class_ = 3
        classcount1[2] = classcount1[2] + 1

    if int(signalcode) >= 33 and int(signalcode) <= 40:
        class_ = 2
        classcount1[1] = classcount1[1] + 1
    


    return class_, classcount1
    


mainprog()