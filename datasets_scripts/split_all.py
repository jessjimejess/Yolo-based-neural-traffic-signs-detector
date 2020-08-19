import os
import shutil
import cv2


ORIGINALANNOTATIONS = "full-gt.csv"
ORIGINALIMAGES = "rtsd-frames"
CLASSLIMIT = 50000
os.makedirs("RUSSIAN_ALL_TRAFFIC_SPLITTED/yield")

imcodes = ["5_19_1","3_24_n10","3_24_n20","3_24_n30","3_24_50","3_24_n40","3_24_n60","3_24_n70","3_24_n80","3_24_n90",
            "3_24_n100","2_4", "2_5","4_2_1","4_2_2","4_2_3","4_2_4","4_2_5","4_1_1","4_1_2","4_1_3","4_1_4","4_1_5"]




def annotationcalc(source, dest, splitted, signalcode):
    img = cv2.imread(source,0)
    height, width = img.shape[:2]

    print(height, width)

    fromx = int(splitted[1])
    fromy = int(splitted[2])
    framewidth = int(splitted[3])
    frameheight = int(splitted[4])
    
    x1 = fromx
    x2 = x1 + framewidth
    y1 = fromy
    y2 = y1 + frameheight
    absx = (x1 + x2)/2.
    absy = (y1 + y2)/2.
    frame_x = absx/width
    frame_y = absy/height
    absheight = frameheight/height
    abswidth = framewidth/width

    class_ = classcalculation(signalcode)
    f = open(dest + "/" + splitted[0].replace(".jpg",".txt"),"a")
    f.write(str(class_) + " " + str(frame_x) + " " + str(frame_y) + " " + str(abswidth) + " " + str(absheight) + "\n")



def mainprog():
    f = open(ORIGINALANNOTATIONS)
    lines = f.readlines()
    classcount1 = 0
    classcount2 = 0
    classcount3 = 0
    classcount4 = 0
    classcount5 = 0
    classcount6 = 0
    classcount7 = 0


    for line in lines:
        splitted = line.split(",")
        signalcode = splitted[5].strip()
        if signalcode in imcodes or signalcode[:2] == "1_":
            source = ORIGINALIMAGES + "/" + splitted[0].strip()
            dest = "RUSSIAN_ALL_TRAFFIC_SPLITTED/yield/" + splitted[0].strip()
            andd = "RUSSIAN_ALL_TRAFFIC_SPLITTED/yield/"
            
            if signalcode == "5_19_1" and classcount1 <= CLASSLIMIT:
                classcount1 = classcount1 + 1
                
            if "3_24" in signalcode and classcount2 <= CLASSLIMIT:
                classcount2 = classcount2 + 1
            
            if (signalcode == "4_2_1" or signalcode == "4_2_2" or signalcode == "4_2_3" or signalcode == "4_2_4" or signalcode == "4_2_5") and classcount3 <= classlimit :
                classcount3 = classcount3 + 1
            
            if (signalcode == "4_1_1" or signalcode == "4_1_2" or signalcode == "4_1_3" or signalcode == "4_1_4" or signalcode == "4_1_5" or signalcode == "4_3")  and classcount3 <= classlimit :
                classcount3 = classcount3 + 1
            
            if signalcode[:2] == "1_" and classcount4 <= CLASSLIMIT:
                classcount4 = classcount4 + 1

            if signalcode == "2_4" and classcount5 <= CLASSLIMIT:
                classcount5 = classcount5 + 1

            if signalcode == "2_5" and classcount7 <= CLASSLIMIT:
                classcount7 = classcount7 + 1

            annotationcalc(source, andd, splitted, signalcode)
            shutil.copy(source, dest)

    print("\n0 peaton: ", classcount1,"\n1 velocidad: ",classcount2,"\n2 direccion: ",classcount3,"\n3 peligro: ",classcount4,"\n4 ceda el paso: ",classcount5,"\n5 stop: ",classcount7)


def classcalculation(signalcode):
    if signalcode == "5_19_1":
        class_ = 0
        
    if "3_24_" in signalcode:
        class_ = 1
    
    if signalcode == "4_2_1" or signalcode == "4_2_2" or signalcode == "4_2_3" or signalcode == "4_2_4" or signalcode == "4_2_5" :
        class_ = 2

    if signalcode == "4_1_1" or signalcode == "4_1_2" or signalcode == "4_1_3" or signalcode == "4_1_4" or signalcode == "4_1_5" :
        class_ = 2

    if signalcode[:2] == "1_":
        class_ = 3

    if signalcode == "2_4":
        class_ = 4

    if signalcode == "2_5":
        class_ = 5

    return class_


if __name__ == "__main__":
    mainprog()