import os
import shutil


originalimageset = ["TS2010\SourceImages", "TS2011\SourceImages"]
originalannotations = ["TS2010\SourceImages", "TS2011\SourceImages"]


greendir = "TS_SPLITTED"
HEIGHT = 576
WIDTH = 720

def annotationcalc(destino, splitted, categoria):

    ansplitted = splitted.split("&")
    
    for annotation in ansplitted:
        if "B02" in annotation:
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

            class_ = categoria
            f = open(destino.replace(".bmp",".txt"),"a")
            f.write(str(class_) + " " + str(framex) + " " + str(framey) + " " + str(framewidth) + " " + str(frameheigth) + "\n")

def mainprog():
    classcount = 0
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
            
            if "B02" in annot:
                source = annotationd + "/" + imgpath
                dest = greendir + "/" + destimgpath
                classcount = classcount + 1
            
                shutil.copy(source, dest)
                annotationcalc(dest,annot,3)


def mainfunction():

    mainprog()

mainfunction()


