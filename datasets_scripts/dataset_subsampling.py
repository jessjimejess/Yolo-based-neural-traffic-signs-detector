import os
import cv2
import random
import numpy as np
import shutil


DATASETDIR = "RUSSIAN_ALL_TRAFFIC_SPLITTED/yield"
AUGMENTATIONDIR = "RUSSIAN_ALL_TRAFFIC_SPLITTED/yield"
DATASETNUMBERS = []


def brightup(imgpath, imgpathblur, type_):
    image = cv2.imread(imgpath.replace(".txt",".jpg"))
    shape = image.shape
    if type_ == "bright":
        randint = random.randint(0,1)
        if randint == 0:
            brightlevel = random.randint(50,70)/100
        
        else:
            brightlevel = random.randint(50,70)/100
    
        contrast = random.randint(-50,50)
        for i in range(shape[0]):
            for j in range(shape[1]):
                image[i][j][0] = np.clip(image[i][j][0] * brightlevel + contrast, 0, 255)
                image[i][j][1] = np.clip(image[i][j][1] * brightlevel + contrast, 0, 255)
                image[i][j][2] = np.clip(image[i][j][2] * brightlevel + contrast, 0, 255)

        cv2.imwrite(imgpathblur.replace(".txt",".jpg") , image) 
        shutil.copy(imgpath, imgpathblur)
    
    elif type_ == "gauss":
        gaussmatrix = np.random.normal(0, 20, shape)
        image = image + gaussmatrix
        cv2.imwrite(imgpathblur.replace(".txt",".jpg") , image) 
        shutil.copy(imgpath, imgpathblur)



def randomdelete(listimages, pedcounter):
    
    numberofd = pedcounter - 6000
    while numberofd > 0 and len(listimages) > 0:
        randints = random.randint(0,len(listimages) - 1)

        imagetodelete = listimages[randints]
        listimages.pop(randints)
        os.remove(DATASETDIR + "/" + imagetodelete[0])
        os.remove(DATASETDIR + "/" + imagetodelete[0].replace("txt", "jpg"))
        numberofd = numberofd - imagetodelete[1]



def dosubsampling(class_number):
    listImages = []
    classcounter = 0
    pedcounter = countdataset()
    pedcounter = pedcounter[0]
    
    listdataset = os.listdir(DATASETDIR)
    for delement in listdataset:
        if ".txt" in delement:
            f = open(DATASETDIR + "/" + delement)
            listLines = f.readlines()
            firstclass = ""
            listclass = [line.split(" ")[0] for line in listLines]

            if len(listclass) == 1 and listclass[0] == "0":
                listImages.append([delement, len(listclass)])
                classcounter = classcounter + 1
            
            else:
                for i,class_ in enumerate(listclass):
                    if listclass[0] == class_ and listclass[0] == "0":
                        if i + 1 == len(listclass):
                            listImages.append([delement, len(listclass)])
                            classcounter = classcounter + len(listclass)
                    
                    else:
                        break
                   
    randomdelete(listImages, pedcounter)
    


def augmentation(type_):
    listImages = []
    listdataset = os.listdir(AUGMENTATIONDIR)
    classcounter = 0
    
    for delement in listdataset:
        imgpath = AUGMENTATIONDIR + "/" + delement
        imgpathblur = AUGMENTATIONDIR + "/bbb_" + delement
        
        if ".txt" in delement:
            f = open(imgpath)
            listLines = f.readlines()
            firstclass = ""
            listclass = [line.split(" ")[0] for line in listLines]
            
            if len(listclass) == 1 and listclass[0] == "5":
                brightup(imgpath,imgpathblur, type_)
                classcounter = classcounter + 1
            
            else:
                for i,class_ in enumerate(listclass):
                    if listclass[0] == class_ and listclass[0] == "5":
                        if i + 1 == len(listclass):
                            brightup(imgpath,imgpathblur, type_)
                    
                    else:
                        break

    
def countdataset():
    listdir = os.listdir(DATASETDIR)
    pedcounter = 0
    speedcounter = 0
    warningcounter = 0
    dircounter = 0
    yieldcounter = 0
    stopcounter = 0

    for element in listdir:
        if ".txt" in element:
            f = open(DATASETDIR + "/" + element)
            lines = f.readlines()
            for line in lines:
                splittedline = line.split(" ")
                if splittedline[0] == "0":
                    pedcounter = pedcounter + 1
                if splittedline[0] == "1":
                    speedcounter = speedcounter + 1
                if splittedline[0] == "2":
                    dircounter = dircounter + 1                
                if splittedline[0] == "3":
                    warningcounter = warningcounter + 1
                if splittedline[0] == "4":
                    yieldcounter = yieldcounter + 1
                if splittedline[0] == "5":
                    stopcounter = stopcounter + 1
        print("ok")        
    print("ped:" , pedcounter, "speed:", speedcounter, "dir:", dircounter, "warning:", warningcounter, "yild:", yieldcounter, "stop:", stopcounter)
    return [pedcounter, speedcounter, dircounter, warningcounter, yieldcounter, stopcounter]

                
                


                







if __name__ == "__main__":
    #dosubsampling(6)
    #countdataset()
    augmentation("bright")
    