import os
import shutil


originalimageset = "LISATS\dayTrain/dayTrain"
originalannotations = "LISATS\Annotations\Annotations\dayTrain"
originalimageset2 = "LISATS\daySequence1/daySequence1/"
originalannotations2 = "LISATS\Annotations\Annotations\daySequence1"
originalimageset3 = "LISATS\daySequence2/daySequence2/"
originalannotations3 = "LISATS\Annotations\Annotations\daySequence2"

greendir = "LISATS_SPLITTED/green"
reddir = "LISATS_SPLITTED/red"
orangedir = "LISATS_SPLITTED/orange"
imcodes = ["go", "stop", "warning"]
HEIGHT = 960
WIDTH = 1280

def annotationcalc(destino, splitted, categoria, imagepath):
    x1 = int(splitted[2])
    y1 = int(splitted[3])
    x2 = int(splitted[4])
    y2 = int(splitted[5])

    absx = (x2 + x1)/2.
    absy = (y2 + y1)/2.

    framex = absx/WIDTH
    framey = absy/HEIGHT

    framewidth = (x2 - x1)/WIDTH
    frameheigth = (y2 - y1)/HEIGHT

    class_ = classcalculation(categoria)
    f = open(destino + "/" + categoria + "_" + imagepath.replace(".jpg",".txt"),"w")
    f.write(str(class_) + " " + str(framex) + " " + str(framey) + " " + str(framewidth) + " " + str(frameheigth))

def readf(f, clase):
    lines = f.readlines()
    for i,line in enumerate(lines):
        if i != 0:
            splitted = line.split(";")
            categoria = splitted[1].strip()
            imagepath = splitted[0].strip().split("/")[1]
        
            if categoria in imcodes:
                if "go" in categoria:
                    source = originalimageset + "/" + clase + "/" + "frames/" + imagepath
                    destino = greendir
            
                if "stop" in categoria:
                    source = originalimageset + "/" + clase + "/" + "frames" + "/" + imagepath
                    destino = reddir

                if "warning" in categoria:
                    source = originalimageset + "/" + clase + "/" + "frames/" + imagepath
                    destino = orangedir

                annotationcalc(destino, splitted, categoria, imagepath)
                shutil.copy(source, destino + "/" + categoria + "_" + imagepath)

def classcalculation(categoria):
    if "go" in categoria:
        class_ = 0
        
    if "stop" in categoria:
        class_ = 1
        
    if "warning" in categoria:
        class_ = 2

    return class_


def readfdaysequence(f, seq):
    if seq == "1":
        src = originalimageset2
    else:
        src = originalimageset3
    lines = f.readlines()
    for i,line in enumerate(lines):
        if i != 0:
            splitted = line.split(";")
            categoria = splitted[1].strip()
            imagepath = splitted[0].strip().split("/")[1]
        
            if categoria in imcodes:
                if "go" in categoria:
                    source = src +  "/" + "frames/" + imagepath
                    destino = greendir
            
                if "stop" in categoria:
                    source = src + "/" + "frames" + "/" + imagepath
                    destino = reddir

                if "warning" in categoria:
                    source = src + "/" + "frames/" + imagepath
                    destino = orangedir

                annotationcalc(destino, splitted, categoria, imagepath)
                shutil.copy(source, destino + "/" + categoria + "_" + imagepath)

def mainfunction():
    

    os.makedirs(greendir)
    os.mkdir(reddir)
    os.mkdir(orangedir)
    
    listaclases = os.listdir(originalannotations)
    
    
    for clase in listaclases:
        f = open(originalannotations + "/" + clase + "/" + "frameAnnotationsBOX.csv")
        readf(f, clase)
        
    f = open(originalannotations2 + "/" + "frameAnnotationsBOX.csv")
    readfdaysequence(f, "1")

    f = open(originalannotations3 + "/" + "frameAnnotationsBOX.csv")
    readfdaysequence(f, "2")
    



mainfunction()


