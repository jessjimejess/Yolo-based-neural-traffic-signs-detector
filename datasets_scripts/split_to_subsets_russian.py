import os
import random
import shutil

validation_subset = "validation_russian"
test_subset = "test_russian"
train_subset = "RUSSIAN_ALL_TRAFFIC_SPLITTED/yield"
VALIDATIONPER = 15
TESTPER = 15


def writetraindata():

        imagelist = os.listdir(train_subset)
        for image in imagelist:
            if ".jpg" in image:
                f = open("objects_list/" + "train.txt", "a")
                f.writelines("data/obj/" + image + "\n")



def splitvalidation():
    
    imagelist = os.listdir(train_subset)
    lenimagelist = len(imagelist)
    validationumber = int(((VALIDATIONPER * lenimagelist) /2 ) / 100)
    
    while(validationumber > 0):
        lenimagelist = len(imagelist)
        randint = random.randint(0,lenimagelist)
        image = imagelist[randint - 1]
            
        validationumber = validationumber - 1
            
        if ".jpg" in image:
                
            imagelist.remove(image)
            imagelist.remove(image.replace(".jpg",".txt"))
            shutil.move(train_subset + "/" + image, validation_subset)
            shutil.move(train_subset + "/" + image.replace(".jpg",".txt"),validation_subset)
        else:
                
            imagelist.remove(image)
            imagelist.remove(image.replace(".txt",".jpg"))
            shutil.move(train_subset + "/" + image, validation_subset)
            shutil.move(train_subset + "/" + image.replace(".txt",".jpg"), validation_subset)
            
            
        f = open("objects_list/" + "validation.txt", "a")
        f.writelines("data/obj/" + image.replace(".txt",".jpg") + "\n")
           

        
def splittest():
    
    
    imagelist = os.listdir(train_subset)
    lenimagelist = len(imagelist)
    validationumber = int(((TESTPER * lenimagelist)/2) / 100)

    while(validationumber > 0):
        lenimagelist = len(imagelist)
        randint = random.randint(0,lenimagelist)
        image = imagelist[randint - 1]
            
        validationumber = validationumber - 1
        if ".jpg" in image:
            imagelist.remove(image)
            imagelist.remove(image.replace(".jpg",".txt"))
            shutil.move(train_subset + "/" + image, test_subset)
            shutil.move(train_subset + "/" + image.replace(".jpg",".txt"), test_subset)
        else:
            imagelist.remove(image)
            imagelist.remove(image.replace(".txt",".jpg"))
            shutil.move(train_subset + "/" + image, test_subset)
            shutil.move(train_subset + "/" + image.replace(".txt",".jpg"), test_subset)
            
            
        f = open("objects_list/" + "test.txt", "a")
        f.writelines("data/obj/" + image.replace(".txt",".jpg") + "\n")



def movetrainset():
    classlist = os.listdir("RUSSIAN_ALL_TRAFFIC_SPLITTED")
    for class_ in classlist:
        
        imagelist = os.listdir("RUSSIAN_ALL_TRAFFIC_SPLITTED/" + class_)
        lenimagelist = len(imagelist)
        trainumber = 3500
        
        if(trainumber > lenimagelist/2):
            moveall(imagelist, class_)
        else:
            while(trainumber > 0):
            
                lenimagelist = len(imagelist)
                print("lenlist: " + str(lenimagelist))
                randint = random.randint(0,lenimagelist)
                print("randint" + str(randint))
                image = imagelist[randint - 1]

                trainumber = trainumber - 1
                if ".jpg" in image:
                    imagelist.remove(image)
                    imagelist.remove(image.replace(".jpg",".txt"))
                    shutil.copy("RUSSIAN_ALL_TRAFFIC_SPLITTED/" + class_ + "/" + image, train_subset)
                    shutil.copy("RUSSIAN_ALL_TRAFFIC_SPLITTED/" + class_ + "/" + image.replace(".jpg",".txt"), train_subset)
                else:
                    imagelist.remove(image)
                    imagelist.remove(image.replace(".txt",".jpg"))
                    shutil.copy("RUSSIAN_ALL_TRAFFIC_SPLITTED/" + class_ + "/" + image, train_subset)
                    shutil.copy("RUSSIAN_ALL_TRAFFIC_SPLITTED/" + class_ + "/" + image.replace(".txt",".jpg"), train_subset)
            


def moveall(imagelist, class_):
    for image in imagelist:
        if ".jpg" in image:
            shutil.copy("RUSSIAN_ALL_TRAFFIC_SPLITTED/" + class_ + "/" + image, train_subset)
            shutil.copy("RUSSIAN_ALL_TRAFFIC_SPLITTED/" + class_ + "/" + image.replace(".jpg",".txt"), train_subset)
        
        else:
            shutil.copy("RUSSIAN_ALL_TRAFFIC_SPLITTED/" + class_ + "/" + image, train_subset)
            shutil.copy("RUSSIAN_ALL_TRAFFIC_SPLITTED/" + class_ + "/" + image.replace(".txt",".jpg"), train_subset)


if __name__ == "__main__":
    
    os.mkdir(validation_subset)
    os.mkdir(test_subset)
    splitvalidation()
    splittest()
    writetraindata()

