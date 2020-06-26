import os
import random
import shutil

validation_subset = "validation"
test_subset = "test"
train_subset = "train"
VALIDATIONPER = 15
TESTPER = 15
IMAGE_SET = 3500      # Final number of images for each set

def writetraindata():

        imagelist = os.listdir(train_subset)
        for image in imagelist:
            if ".jpg" in image:
                f = open("objects_list/" + "train.txt", "a")
                f.writelines("data/obj/" + image + "\n")



def splitlisats():
   
    imagelist = os.listdir(train_subset)
    lenimagelist = len(imagelist)
    validationumber = int((VALIDATIONPER * lenimagelist)/2) / 100
    while(validationumber > 0):
        lenimagelist = len(imagelist)
        randint = random.randint(0,lenimagelist - 1)
        image = imagelist[randint]
            
        validationumber = validationumber - 1
        print("----")
        if ".jpg" in image:
            print("1")
            imagelist.remove(image)
            imagelist.remove(image.replace(".jpg",".txt"))
            shutil.move(train_subset + "/" + image, validation_subset)
            shutil.move(train_subset + "/" + image.replace(".jpg",".txt"),validation_subset)
        else:
            print("2")
            imagelist.remove(image)
            imagelist.remove(image.replace(".txt",".jpg"))
            shutil.move("train/" + image, validation_subset)
            shutil.move("train/" + image.replace(".txt",".jpg"), validation_subset)
            
            
        f = open("objects_list/" + "validation.txt", "a")
        f.writelines("data/obj/" + image.replace(".txt",".jpg") + "\n")
           
def splittest():
    
        
    imagelist = os.listdir(train_subset)
    lenimagelist = len(imagelist)
    validationumber = int((TESTPER * lenimagelist)/2) / 100

    while(validationumber > 0):
        lenimagelist = len(imagelist)
        randint = random.randint(0,lenimagelist - 1)
        image = imagelist[randint]
            
        validationumber = validationumber - 1
        if ".jpg" in image:
            imagelist.remove(image)
            imagelist.remove(image.replace(".jpg",".txt"))
            shutil.move("train/" + image, test_subset)
            shutil.move("train/" + image.replace(".jpg",".txt"), test_subset)
        else:
            imagelist.remove(image)
            imagelist.remove(image.replace(".txt",".jpg"))
            shutil.move("train/" + image, test_subset)
            shutil.move("train/" + image.replace(".txt",".jpg"), test_subset)
            
            
        f = open("objects_list/" + "test.txt", "a")
        f.writelines("data/obj/" + image.replace(".txt",".jpg") + "\n")
    
def movetrainset():
    classlist = os.listdir("LISATS_SPLITTED")
    for class_ in classlist:
        
        imagelist = os.listdir("LISATS_SPLITTED/" + class_)
        lenimagelist = len(imagelist)
        trainumber = 3500
        
        if(trainumber > lenimagelist):
            moveall(imagelist, class_)
        else:
            while(trainumber > 0):
            
                lenimagelist = len(imagelist)
                randint = random.randint(0,lenimagelist)
                image = imagelist[randint - 1]
            
                trainumber = trainumber - 1
                if ".jpg" in image:
                    print(image)
                    imagelist.remove(image)
                    imagelist.remove(image.replace(".jpg",".txt"))
                    shutil.copy("LISATS_SPLITTED/" + class_ + "/" + image, train_subset)
                    shutil.copy("LISATS_SPLITTED/" + class_ + "/" + image.replace(".jpg",".txt"), train_subset)
                else:
                    print(image)
                    imagelist.remove(image)
                    imagelist.remove(image.replace(".txt",".jpg"))
                    shutil.copy("LISATS_SPLITTED/" + class_ + "/" + image, train_subset)
                    shutil.copy("LISATS_SPLITTED/" + class_ + "/" + image.replace(".txt",".jpg"), train_subset)
            


def moveall(imagelist, class_):
    for image in imagelist:
        if ".jpg" in image:
            print(image)
            shutil.copy("LISATS_SPLITTED/" + class_ + "/" + image, train_subset)
            shutil.copy("LISATS_SPLITTED/" + class_ + "/" + image.replace(".jpg",".txt"), train_subset)

        else:
            print(image)
            shutil.copy("LISATS_SPLITTED/" + class_ + "/" + image, train_subset)
            shutil.copy("LISATS_SPLITTED/" + class_ + "/" + image.replace(".txt",".jpg"), train_subset)





def mainfunc():
   
    os.mkdir(validation_subset)
    os.mkdir(test_subset)
    os.mkdir(train_subset)
    movetrainset()
    splitlisats()
    splittest()
    writetraindata()

mainfunc()