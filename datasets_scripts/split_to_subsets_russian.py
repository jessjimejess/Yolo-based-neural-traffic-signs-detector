import os
import random
import shutil

VALIDATION_SUBSET = "validation_russian"
TEST_SUBSET = "test_russian"
TRAIN_SUBSET = "RUSSIAN_ALL_TRAFFIC_SPLITTED/yield"
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
            imagelist.remove(image.replace(".jpg",".txt"))
        
        else:
            imagelist.remove(image.replace(".txt",".jpg"))
        
        shutil.move(TRAIN_SUBSET + "/" + image, VALIDATION_SUBSET)
        shutil.move(TRAIN_SUBSET + "/" + image.replace(".txt",".jpg"), VALIDATION_SUBSET)
            
            
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
        imagelist.remove(image)

        if ".jpg" in image:
            imagelist.remove(image.replace(".jpg",".txt"))
           
        else:
            imagelist.remove(image.replace(".txt",".jpg"))
            
        shutil.move(TRAIN_SUBSET + "/" + image, TEST_SUBSET)
        shutil.move(TRAIN_SUBSET + "/" + image.replace(".jpg",".txt"), TEST_SUBSET)
            
        f = open("objects_list/" + "test.txt", "a")
        f.writelines("data/obj/" + image.replace(".txt",".jpg") + "\n")


if __name__ == "__main__":
    
    os.mkdir(VALIDATION_SUBSET)
    os.mkdir(TEST_SUBSET)
    splitvalidation()
    splittest()
    writetraindata()

