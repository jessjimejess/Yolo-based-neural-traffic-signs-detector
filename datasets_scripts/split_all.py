import os
import shutil
import cv2


originalannotations = "full-gt.csv"
originalimages = "rtsd-frames"
classlimit = 3500
os.makedirs("RUSSIAN_ALL_TRAFFIC_SPLITTED/yield")
# os.mkdir("RUSSIAN_ALL_TRAFFIC_SPLITTED/speed")
# os.mkdir("RUSSIAN_ALL_TRAFFIC_SPLITTED/speed30")
# os.mkdir("RUSSIAN_ALL_TRAFFIC_SPLITTED/speed40")
# os.mkdir("RUSSIAN_ALL_TRAFFIC_SPLITTED/speed50")
# os.mkdir("RUSSIAN_ALL_TRAFFIC_SPLITTED/speed60")
# os.mkdir("RUSSIAN_ALL_TRAFFIC_SPLITTED/speed70")
# os.mkdir("RUSSIAN_ALL_TRAFFIC_SPLITTED/speed80")
# os.mkdir("RUSSIAN_ALL_TRAFFIC_SPLITTED/speed100")
#os.mkdir("RUSSIAN_ALL_TRAFFIC_SPLITTED/yield")
# os.mkdir("RUSSIAN_ALL_TRAFFIC_SPLITTED/prohib")
# os.mkdir("RUSSIAN_ALL_TRAFFIC_SPLITTED/stop")
# os.mkdir("RUSSIAN_ALL_TRAFFIC_SPLITTED/direction")
# os.mkdir("RUSSIAN_ALL_TRAFFIC_SPLITTED/danger")

imcodes = ["5_19_1","3_24_n20","3_24_n30","3_24_50","3_24_n40","3_24_n60","3_24_n70","3_24_n80",
            "3_24_n100","2_4","3_1", "2_5","4_2_1","4_2_2","4_2_3","4_2_4","4_2_5","4_1_1","4_1_2","4_1_3","4_1_4","4_1_5"]

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
    f = open(originalannotations)
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
            if signalcode == "5_19_1" and classcount1 <= classlimit:
                source = originalimages + "/" + splitted[0].strip()
                dest = "RUSSIAN_ALL_TRAFFIC_SPLITTED/yield/" + splitted[0].strip()
                andd = "RUSSIAN_ALL_TRAFFIC_SPLITTED/yield/"
                classcount1 = classcount1 + 1
                
            if "3_24" in signalcode and classcount2 <= classlimit:
                source = originalimages + "/" + splitted[0].strip()
                dest = "RUSSIAN_ALL_TRAFFIC_SPLITTED/yield/" + splitted[0].strip()
                andd = "RUSSIAN_ALL_TRAFFIC_SPLITTED/yield/"
                classcount2 = classcount2 + 1
            
            if (signalcode == "4_2_1" or signalcode == "4_2_2" or signalcode == "4_2_3" or signalcode == "4_2_4" or signalcode == "4_2_5") and classcount3 <= classlimit :
                source = originalimages + "/" + splitted[0].strip()
                dest = "RUSSIAN_ALL_TRAFFIC_SPLITTED/yield/" + splitted[0].strip()
                andd = "RUSSIAN_ALL_TRAFFIC_SPLITTED/yield/"
                classcount3 = classcount3 + 1
            
            if (signalcode == "4_1_1" or signalcode == "4_1_2" or signalcode == "4_1_3" or signalcode == "4_1_4" or signalcode == "4_1_5")  and classcount3 <= classlimit :
                source = originalimages + "/" + splitted[0].strip()
                dest = "RUSSIAN_ALL_TRAFFIC_SPLITTED/yield/" + splitted[0].strip()
                andd = "RUSSIAN_ALL_TRAFFIC_SPLITTED/yield/"
                classcount3 = classcount3 + 1
            
            if signalcode[:2] == "1_" and classcount4 <= classlimit:
                source = originalimages + "/" + splitted[0].strip()
                dest = "RUSSIAN_ALL_TRAFFIC_SPLITTED/yield/" + splitted[0].strip()
                andd = "RUSSIAN_ALL_TRAFFIC_SPLITTED/yield/"
                classcount4 = classcount4 + 1

            # if signalcode == "3_24_n40":
            #     source = originalimages + "/" + splitted[0].strip()
            #     dest = "RUSSIAN_ALL_TRAFFIC_SPLITTED/speed40/" + signalcode + splitted[0].strip()
            #     andd = "RUSSIAN_ALL_TRAFFIC_SPLITTED/speed40/"

            # if signalcode == "3_24_n60":
            #     source = originalimages + "/" + splitted[0].strip()
            #     dest = "RUSSIAN_ALL_TRAFFIC_SPLITTED/speed60/" + signalcode + splitted[0].strip()
            #     andd = "RUSSIAN_ALL_TRAFFIC_SPLITTED/speed60/"

            # if signalcode == "3_24_n80":
            #     source = originalimages + "/" + splitted[0].strip()
            #     dest = "RUSSIAN_ALL_TRAFFIC_SPLITTED/speed80/" + signalcode + splitted[0].strip()
            #     andd = "RUSSIAN_ALL_TRAFFIC_SPLITTED/speed80/"

            # if signalcode == "3_24_n100":
            #     source = originalimages + "/" + splitted[0].strip()
            #     dest = "RUSSIAN_ALL_TRAFFIC_SPLITTED/speed100/" + signalcode + splitted[0].strip()
            #     andd = "RUSSIAN_ALL_TRAFFIC_SPLITTED/speed100/"

            if signalcode == "2_4" and classcount5 <= classlimit:
                source = originalimages + "/" + splitted[0].strip()
                dest = "RUSSIAN_ALL_TRAFFIC_SPLITTED/yield/" + splitted[0].strip()
                andd = "RUSSIAN_ALL_TRAFFIC_SPLITTED/yield/"
                classcount5 = classcount5 + 1

            if signalcode == "3_1" and classcount6 <= classlimit:
                source = originalimages + "/" + splitted[0].strip()
                dest = "RUSSIAN_ALL_TRAFFIC_SPLITTED/yield/" + splitted[0].strip()
                andd = "RUSSIAN_ALL_TRAFFIC_SPLITTED/yield/"
                classcount6 = classcount6 + 1

            if signalcode == "2_5" and classcount7 <= classlimit:
                source = originalimages + "/" + splitted[0].strip()
                dest = "RUSSIAN_ALL_TRAFFIC_SPLITTED/yield/" + splitted[0].strip()
                andd = "RUSSIAN_ALL_TRAFFIC_SPLITTED/yield/"
                classcount7 = classcount7 + 1

            annotationcalc(source, andd, splitted, signalcode)
            shutil.copy(source, dest)

    print("\n1: ", classcount1,"\n2: ",classcount2,"\n3: ",classcount3,"\n4: ",classcount4,"\n5: ",classcount5,"\n6: ",classcount6,"\n7: ",classcount7)

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

    # if signalcode == "3_24_n40":
    #     class_ = 4

    # if signalcode == "3_24_n60":
    #     class_ = 4

    # if signalcode == "3_24_n80":
    #     class_ = 4

    # if signalcode == "3_24_n100":
    #     class_ = 4

    if signalcode == "2_4":
        class_ = 4
            
    if signalcode == "3_1":
        class_ = 5

    if signalcode == "2_5":
        class_ = 6

    return class_


mainprog()