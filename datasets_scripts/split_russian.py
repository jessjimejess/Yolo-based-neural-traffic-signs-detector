import os
import shutil


originalimageset = "RUSSIAN TRAFFIC/d3/train"
originalannotations = "RUSSIAN TRAFFIC/rtsd-d3-gt"



def mainfunction():
    

    os.makedirs("RUSSIAN_TRAFFIC_SPLITTED/blue_border")
    os.mkdir("RUSSIAN_TRAFFIC_SPLITTED/blue_rect")
    os.mkdir("RUSSIAN_TRAFFIC_SPLITTED/danger")
    os.mkdir("RUSSIAN_TRAFFIC_SPLITTED/mandatory")
    os.mkdir("RUSSIAN_TRAFFIC_SPLITTED/prohibitory")
    os.mkdir("RUSSIAN_TRAFFIC_SPLITTED/main_road")


    for classfolder in os.listdir(originalannotations):
        annotationsfile = originalannotations + "/" + classfolder + "/train_gt.csv"

        f = open(annotationsfile)
        lines = f.readlines()

        for i,line in enumerate(lines):
            if i != 0:
                imagename = line.split(",")[0]
                originaldir = originalimageset + "/"+ imagename
                copydir = "RUSSIAN_TRAFFIC_SPLITTED/" + classfolder
                shutil.copy(originaldir, copydir)

                


def pedestriansegmentation():
    os.mkdir("RUSSIAN_TRAFFIC_SPLITTED/blue_rect_pedestrian")
    annotations = originalannotations + "/blue_rect/train_gt.csv"
    f = open(annotations)

    lines = f.readlines()

    for i,line in enumerate(lines):
        if i !=0:
            splittedlines = line.split(",")
            print(splittedlines[5])
            if splittedlines[5].strip() == "5_19_1":
                originalimage = originalimageset + "/" + splittedlines[0]
                shutil.copy(originalimage, "RUSSIAN_TRAFFIC_SPLITTED/blue_rect_pedestrian")


def speedsegmentation():
    os.mkdir("RUSSIAN_TRAFFIC_SPLITTED/prohibitory_speed")
    annotations = originalannotations + "/prohibitory/train_gt.csv"
    f = open(annotations)

    lines = f.readlines()

    for i,line in enumerate(lines):
        if i !=0:
            splittedlines = line.split(",")
            print(splittedlines[5])
            if "3_24_n" in splittedlines[5].strip():
                originalimage = originalimageset + "/" + splittedlines[0]
                shutil.copy(originalimage, "RUSSIAN_TRAFFIC_SPLITTED/prohibitory_speed")
    




# mainfunction()
# pedestriansegmentation()
# speedsegmentation()

