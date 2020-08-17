import os
import shutil
import cv2
import re

originalimageset = ["TS2010\SourceImages", "TS2011\SourceImages"]
originalannotations = ["TS2010\SourceImages", "TS2011\SourceImages"]


greendir = "TS_SPLITTED"
HEIGHT = 576
WIDTH = 720

def writetxt(annotation, destino, classcount):
    do = 0
    regex = re.compile("A\d{2}")

    if "B02" in annotation:
        classcount[0] = classcount[0] + 1
        return 1, "5", classcount
        

    if "B31" in annotation:
        classcount[1] = classcount[1] + 1
        return 1, "1", classcount
        

    if "C02" in annotation:
        classcount[2] = classcount[2] + 1
        return 1, "0", classcount
        

    if regex.search(annotation):
        classcount[3] = classcount[3] + 1
        return 1, "3", classcount
        

    if ("B51" in annotation or "B57" in annotation or "B570" in annotation 
        or "B52" in annotation or "B53" in annotation or "B54" in annotation
        or "B59" in annotation or "B60" in annotation or "B62" in annotation):
        
        classcount[4] = classcount[4] + 1
        return 1, "2", classcount

    if "B01" in annotation:
        classcount[5] = classcount[5] + 1
        return 1, "4", classcount
        
        
    return 0, None, classcount
        



def annotationcalc(destino, splitted, classcount):
    ansplitted = splitted.split("&")
    
    for annotation in ansplitted:
        
        index = annotation.find("(")
        index2 = annotation.find(")")
        cleanannotation = annotation[index:index2].replace("x=", "").replace("y=","").replace("w=","").replace("h=","").replace("(","").replace(")","")
        splattributes = cleanannotation.split(",")
        x1 = int(splattributes[0])
        y1 = int(splattributes[1])
        x2 = int(splattributes[0]) + int(splattributes[2])
        y2 = int(splattributes[0]) + int(splattributes[3])

        absx = (x2 + x1)/2.
        absy = (y2 + y1)/2.

        framex = absx/WIDTH
        framey = absy/HEIGHT

        framewidth = (x2 - x1)/WIDTH
        frameheigth = (y2 - y1)/HEIGHT


        do, class_, classcount = writetxt(annotation, destino, classcount)
        
        if do == 1:
            f = open(destino.replace(".jpg",".txt"),"a")
            f.write(str(class_) + " " + str(framex) + " " + str(framey) + " " + str(framewidth) + " " + str(frameheigth) + "\n")
            do = 0

    return classcount

def mainprog():
    classcount = [0,0,0,0,0,0]

    os.makedirs(greendir)
    
    for i,annotationd in enumerate(originalannotations):

        f = open(annotationd + "/sources.log")
        lines = f.readlines()
    
        for line in lines:
            splitted = line.split(" ")
            annot = splitted[3]
            imgpath = splitted[0].strip()
            if i == 0:
                destimgpath = "2010_" + splitted[0].strip()
            else:
                destimgpath = "2011_" + splitted[0].strip()
            
            if "B02" in annot or "B31" in annot:
                source = annotationd + "/" + imgpath
                dest = greendir + "/" + destimgpath.replace(".bmp",".jpg")

                image = cv2.imread(source)
                cv2.imwrite(dest, image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
                classcount = annotationcalc(dest,annot, classcount)
                
                
    print(classcount)

def mainfunction():

    mainprog()

mainfunction()


