import os
import shutil
import cv2


originalannotations = "LISA/allAnnotations.csv"
originalimages = "LISA/"
destimages = "LISA_SPLITTED"
os.mkdir(destimages)

def annotationcalc(source, dest, splitted, signalcode):
    
    img = cv2.imread(source,0)
    height, width = img.shape[:2]

    print(height, width)

    x1 = int(splitted[2])
    x2 = int(splitted[4])

    y1 = int(splitted[3])
    y2 = int(splitted[5])

    absheight = (y2 - y1)/height
    abswidth = (x2 - x1)/width

    centerx = (x2 + x1)/2
    centery = (y2 + y1)/2

    absx = centerx/width
    absy = centery/height


    class_ = classcalculation(signalcode)
    f = open(dest.replace(".png",".txt"),"a")
    f.write(str(class_) + " " + str(absx) + " " + str(absy) + " " + str(abswidth) + " " + str(absheight) + "\n")



def mainprog():
    f = open(originalannotations)
    lines = f.readlines()
    classcount1 = 0

    for i,line in enumerate(lines):
        if i == 0:
            continue

        splitted = line.split(";")
        signalcode = splitted[1].strip()
        filepath = splitted[0].strip()
        listfilepath = filepath.split("/")
        filename = listfilepath[2]

        if signalcode == "stop":
            source = originalimages + filepath
            dest = destimages + "/" + filename
            classcount1 = classcount1 + 1
            image = cv2.imread(source)
            cv2.imwrite(dest.replace(".png",".jpg"), image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
            annotationcalc(source, dest, splitted, signalcode)
    
    print(classcount1)



def classcalculation(signalcode):
    if signalcode == "stop":
        class_ = 5

    return class_
    

if __name__ == "__main__":
    mainprog()