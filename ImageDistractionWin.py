import os
import random
import time
import getpass

#Name: ImagePrinterWin.py
#Description: ImagePrinterWin takes no input, it simply decides to open up a random amount
#   of imagines from 25 to 200 from the user's picture folder in windows. Each imagine is randomly
#   picked and opened at 1 to 5 second intervals.

#Image Printer Function
#Purpose: Does the main bulk work of opening up images on 1 to 5 second intervals
#Input: Amount(Int): Random number from 25 to 200 to decide how many images are to be opened
#Output: Opens up 25 to 200 images
def ImagePrinter(Amount):
    i = 0
    #Obtains the User and creates a path to their pictures directory
    user = getpass.getuser()
    folder= "C:\\"+ "Users" + "\\" + user + "\\" + "Pictures"
    print(folder)
    #A while look that runs an an amount of times equal to the amount
    while i < Amount:
        #Randomly chooses a picture to open
        a = random.choice(os.listdir(folder))
        a = folder + "\\" + a
        os.system(a)
        i = i+1
        #delays each cycle by 1 to 10 seconds for maximum annoyance
        delay = random.randint(1, 5)
        time.sleep(delay)


def main():
    #Randomly chooses number of images to open up from 25 to 200. Can be modified
    x = random.randint(25,200)
    ImagePrinter(x)
main()



