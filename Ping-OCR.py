import tkinter as tk
from PIL import ImageTk, Image
import ctypes
import cv2
#import pytesseract
import pyocr
import pyocr.builders
from datetime import datetime, timedelta
import glob
import numpy as np
import re
import plotly as px
import time
import os
import pyscreenshot
import platform
from pathlib import Path


# CSGO - 1354 875 1570 1003
# FORTNITE - 421 2 500 44

__dir__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
program_start = datetime.now().strftime("%d%m%y%H%M")

Path(os.path.join(__dir__, "images")).mkdir(parents = True, exist_ok = True) 
Path(os.path.join(__dir__, "images_dpi")).mkdir(parents = True, exist_ok = True) 
Path(os.path.join(__dir__, "ping_data")).mkdir(parents = True, exist_ok = True) 


def make_screenshots(bboxNum):

        duration = input("How long should the script be taking screenshot (in minutes e.g. 10)\n")

        time.sleep(7)

        # Setting start time and end time, so while loop for screenshot taking ends after (duration) minutes
        start = datetime.now()

        ## How long the script takes screenshots
        #duration = 0.1 # in minutes

        end = start + timedelta(minutes = float(duration))
        Path(os.path.join(__dir__, "images", program_start)).mkdir(parents = True, exist_ok = True) 

        # Taking screenshots and saving them
        while datetime.now() < end:
            im = pyscreenshot.grab(bbox = (bboxNum)) # bbox = (window placement and size)
            dt = datetime.now()
            fname = os.path.join(__dir__, "images",program_start, "screenshot_{}.{}.png".format(dt.strftime("%H%M_%S"), dt.microsecond // 100000))
            #fname = "C:/Users/Miha_Plume/Desktop/Plume/Ping-OCR/images/pic_{}.{}.png".format(dt.strftime("%H%M_%S"), dt.microsecond // 100000)
            im.save(fname, 'png')
            time.sleep(0.4) # taking a screenshot every 0.5s
        
        print("Screenshot area coordinates (manually enter in the same order): ", bboxNum)
        

class GUI(tk.Tk):
    def __init__(self):

        # Code for taking a screenshot of your screen and allowing you to draw on it and define a rectangle as area of screenshoting

        super().__init__()

        if(platform.system() == "Windows"):
            user32 = ctypes.windll.user32
            user32.SetProcessDPIAware()

        

        self.withdraw()
        self.attributes('-fullscreen', False)

        self.canvas = tk.Canvas()
        self.canvas.pack(fill="both",expand=True)

        image = pyscreenshot.grab()
        self.image = ImageTk.PhotoImage(image)
        self.photo = self.canvas.create_image(0,0,image=self.image,anchor="nw")

        self.x, self.y = 0, 0
        self.rect, self.start_x, self.start_y = None, None, None
        self.deiconify()

        self.canvas.tag_bind(self.photo,"<ButtonPress-1>", self.on_button_press)
        self.canvas.tag_bind(self.photo,"<B1-Motion>", self.on_move_press)
        self.canvas.tag_bind(self.photo,"<ButtonRelease-1>", self.on_button_release)

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, outline='red')

    def on_move_press(self, event):
        curX, curY = (event.x, event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)

    def on_button_release(self, event):
        bbox = self.canvas.bbox(self.rect)
        self.withdraw()
        self.make_screenshots(bbox)
    
    def make_screenshots(self, bboxNum):  ## Function is not a duplucate, this one is for the screenshot input version
        
        duration = input("How long should the script be taking screenshot (in minutes e.g. 10)\n")

        time.sleep(5)

        # Setting start time and end time, so while loop for screenshot taking ends after (duration) minutes
        start = datetime.now()

        ## How long the script takes screenshots
        #duration = 0.1 # in minutes

        Path(os.path.join(__dir__, "images", program_start)).mkdir(parents = True, exist_ok = True) 

        end = start + timedelta(minutes = float(duration))
        screenshot_number = 0
        # Taking screenshots and saving them
        while datetime.now() < end:
            im = pyscreenshot.grab(bbox = (bboxNum)) # bbox = (window placement and size)
            dt = datetime.now()
            fname = os.path.join(__dir__, "images",program_start, "screenshot_{}__{}.png".format(dt.strftime("%H%M_%S"), screenshot_number))
            #fname = "C:/Users/Miha_Plume/Desktop/Plume/Ping-OCR/images/pic_{}.{}.png".format(dt.strftime("%H%M_%S"), dt.microsecond // 100000)
            im.save(fname, 'png')
            screenshot_number += 1
            time.sleep(0.4) # taking a screenshot every 0.5s
        
        print("Screenshot area coordinates", bboxNum)
        root.quit()   

print("\n")


inputType = input("Enter S if you want to select area with screenshot or K for keyboard input: K\n")


if(inputType == "S"):

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    input("Press enter to start the screenshot sellection area - I recommend you to already have the game of choice open and ping displayed at this point")

    time.sleep(7) # Wait for 10 seconds so you can open your game

    root = GUI()

    root.mainloop()

elif (inputType == "K"):
    bbox = [0,0,0,0]
    bbox[0] = int(input("Enter start of width: "))
    bbox[1] = int(input("Enter start of height:"))
    bbox[2] = int(input("Enter end of width:"))
    bbox[3] = int(input("Enter end of height:"))

    #print(bbox)

    make_screenshots(bbox)

else:
    print("Next time, please enter a valid command!")
    exit()

print("done Screenshoting")

def resize_images():
    
    # Opening all screenshots
    #mages=glob.glob("C:/Users/Miha_Plume/Desktop/Plume/Ping-OCR/images/*.png")
    images=glob.glob(os.path.join(__dir__, "images", program_start, "*.png"))

    for image in images:
        set_image_dpi(image)

def set_image_dpi(img):

    # Setting the dpi of the images to 300 and saving them to a new folder
    im = Image.open(img)
    
    

    length_x, width_y = im.size
    factor = min(1, float(1024.0 / length_x))
    size = int(factor * length_x), int(factor * width_y)
    im_resized = im.resize(size, Image.ANTIALIAS)
    #im_resized.save("C:/Users/Miha_Plume/Desktop/Plume/Ping-OCR/images_dpi/{}".format(img.split('\\')[1]), dpi=(300, 300))
  
    im_resized.save(os.path.join(__dir__, "images_dpi",program_start, "s{}".format(img.lstrip(os.path.join(__dir__ , "Ping-OCR", "images", program_start)))), dpi=(300, 300))

def OCR_ping_read():
    
    # Opening all screenshots
    #images=glob.glob("C:/Users/Miha_Plume/Desktop/Plume/Ping-OCR/images_dpi/*.png")
    images=glob.glob(os.path.join(__dir__, "images_dpi",program_start, "*.png"))

    custom_config = r'--oem 3 --psm 6'

    tool = pyocr.get_available_tools()[0]
    lang = tool.get_available_languages()[1]

    pingArr = []
    allPings = 0
    failedPing = 0
    failed = 0

    # OCR loop
    for image in images:
        allPings += 1
        
        img = cv2.imread(image)

        imgOCR = Image.fromarray(img)
        
        # Editing the image so the OCR is more accurate 
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # img = cv2.medianBlur(img,1) # noise removal 
        # img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1] # 0 and 1 image (black or white)

        txt_no_edit = tool.image_to_string(imgOCR, lang = "eng", builder = pyocr.builders.TextBuilder())

        if (len([int(s) for s in txt_no_edit.split() if s.isdigit()]) > 0): # If there is no number in the string simply skip that measurment
                pingArr.append([int(s) for s in txt_no_edit.split() if s.isdigit()][0])
        else:
            kernel = np.ones((2,2),np.uint8)
            img =  cv2.dilate(img, kernel, iterations = 1)
            kernel = np.ones((1,1),np.uint8)
            img = cv2.erode(img,kernel,iterations = 3)
            img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = cv2.threshold(img,0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1] # 0 and 1 image (black or white)
            cv2.Canny(img, 100, 200)
            imgOCR = Image.fromarray(img)

            txt_edit = tool.image_to_string(imgOCR, lang = "eng", builder = pyocr.builders.TextBuilder())
            
            if (len([int(s) for s in txt_edit.split() if s.isdigit()]) > 0): # If there is no number in the string simply skip that measurment
                pingArr.append([int(s) for s in txt_edit.split() if s.isdigit()][0])

            else:
                img = cv2.bitwise_not(img)
                imgOCR = Image.fromarray(img)

                txt_edit_inverse = tool.image_to_string(imgOCR, lang = "eng", builder = pyocr.builders.TextBuilder())

                if (len([int(s) for s in txt_edit_inverse.split() if s.isdigit()]) > 0): # If there is no number in the string simply skip that measurment
                    pingArr.append([int(s) for s in txt_edit_inverse.split() if s.isdigit()][0])

                else:
                    failed += 1


        
    latency = []
    #failed = {}

    return pingArr, allPings, failed

    # for ping in pingArr:
    #     allPings += 1
        
    #     # Extracting just the number from the string | e.g. ping: 24 ms - 24
    #     if (len([int(s) for s in ping.split() if s.isdigit()]) > 0): # If there is no number in the string simply skip that measurment
    #             latency.append([int(s) for s in ping.split() if s.isdigit()][0])
                    
    #     else:
    #         failedPing +=1
    #         failed[allPings] = ping

    # return latency, allPings, failedPing, failed

    

def OCR():
    
    t0 = time.time()
    
    #########
    # You can use this code if you don't want to add tesseract install folder to path / something isn't working
    # accessing tesseract executable -> change to your destination!!
    # pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe' 
    #########

    input("Press enter to start the OCR")

    Path(os.path.join(__dir__, "images_dpi", program_start)).mkdir(parents = True, exist_ok = True) 

    resize_images()

    latency, aPing, failed = OCR_ping_read()

    print("All ping: ", aPing)
    # print("Failed pings: ", fPing)
    print("These are all the failed pings with their corresponding OCR string:", failed)

    if(len(latency) < 1):
        print("Something went wrong during OCR, please try to optimize the screenshots (placement, backrgound...)")
        exit()

    for i  in range(len(latency)):
        if i < len(latency)-10:
            if latency[i] > latency[i-1]*10 and latency[i] > latency[i+1]*10 and latency[i] > latency[i+2]*10 and latency[i] > latency[i+3]*10:
                latency.pop(i)   

    timeOfMeasurment = str(datetime.now().strftime("%H%M_%S"))
    timeOfMeasurment = timeOfMeasurment.split(" ")[0]
    data_fName = os.path.join(__dir__, "ping_data", "ping-data-{}.csv.".format(timeOfMeasurment))

    np.savetxt(data_fName, # Saving the CSV file 
            latency,
            delimiter =", ", 
            fmt ='% s')

    data = np.genfromtxt(data_fName, delimiter = ",") # Reading the CSV file

    fig = px.plot(data, title='CSGO - Ping', kind="line") # Plotting the graph
    
    fig.show()


#time.sleep(2)

OCR()