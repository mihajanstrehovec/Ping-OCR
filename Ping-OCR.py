import tkinter as tk
from PIL import ImageGrab, ImageTk, Image
from ctypes import windll
import cv2
import pytesseract
from datetime import datetime, timedelta
import glob
import numpy as np
import re
import pandas as pd
import plotly as px
import time


class GUI(tk.Tk):
    def __init__(self):

        # Code for taking a screenshot of your screen and allowing you to draw on it and define a rectangle as area of screenshoting

        super().__init__()

        user32 = windll.user32
        user32.SetProcessDPIAware()

        self.withdraw()
        self.attributes('-fullscreen', False)

        self.canvas = tk.Canvas()
        self.canvas.pack(fill="both",expand=True)

        image = ImageGrab.grab()
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
    
    def make_screenshots(self, bboxNum):
        
        

        time.sleep(10)

        # Setting start time and end time, so while loop for screenshot taking ends after (duration) minutes
        start = datetime.now()

        ## How long the script takes screenshots
        duration = 0.1 # in minutes

        end = start + timedelta(minutes = duration)

        # Taking screenshots and saving them
        while datetime.now() < end:
            im = ImageGrab.grab(bbox = (bboxNum)) # bbox = (window placement and size)
            dt = datetime.now()
            fname = "C:/Users/Miha_Plume/Desktop/Plume/Ping-OCR/images/pic_{}.{}.png".format(dt.strftime("%H%M_%S"), dt.microsecond // 100000)
            im.save(fname, 'png')
            time.sleep(0.4) # taking a screenshot every 0.5s
        

        root.quit()   

print("\n")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

input("Press enter to start the screenshot sellection area - I recommend you to already have the game of choice open and ping displayed at this point")

time.sleep(10) # Wait for 10 seconds so you can open your game

root = GUI()

root.mainloop()

print("done Screenshoting")

def resize_images():
    
    # Opening all screenshots
    images=glob.glob("C:/Users/Miha_Plume/Desktop/Plume/Ping-OCR/images/*.png")

    for image in images:
        set_image_dpi(image)

def set_image_dpi(img):

    # Setting the dpi of the images to 300 and saving them to a new folder
    im = Image.open(img)
    length_x, width_y = im.size
    factor = min(1, float(1024.0 / length_x))
    size = int(factor * length_x), int(factor * width_y)
    im_resized = im.resize(size, Image.ANTIALIAS)
    im_resized.save("C:/Users/Miha_Plume/Desktop/Plume/Ping-OCR/images_dpi/{}".format(img.split('\\')[1]), dpi=(300, 300))

def OCR_ping_read():
    
    # Opeinng all screenshots
    images=glob.glob("C:/Users/Miha_Plume/Desktop/Plume/Ping-OCR/images_dpi/*.png")

    custom_config = r'--oem 3 --psm 6'

    pingArr = []

    # OCR loop
    for image in images:
        
        img = cv2.imread(image)
        
        # Editing the image so the OCR is more accurate 
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.medianBlur(img,1) # noise removal 
        img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1] # 0 and 1 image (black or white)
        

        print(pytesseract.image_to_string(img, config=custom_config))
        pingArr.append(pytesseract.image_to_string(img, config=custom_config)) # the OCR algorithm tesseract

        
    latency = []

    for ping in pingArr:
        
        # Extracting just the number from the string | e.g. ping: 24 ms - 24
        if (not re.findall(r'\b\d+\b', ping)) == False: # If there is no number in the string simply skip that measurment
                latency.append(re.findall(r'\b\d+\b', ping)[0]) #

    return latency

    

def OCR():
    
    t0 = time.time()
   
    # You can implement this if you don't want to add tesseract install folder to path / something isn't working
    # accessing tesseract executable -> change to your destination!!
    # pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe' 

    input("Press enter to start the OCR")

    resize_images()

    latency = OCR_ping_read()

    timeOfMeasurment = str(datetime.now())
    timeOfMeasurment = timeOfMeasurment.split(" ")[0]
   

    np.savetxt("C:/Users/Miha_Plume/Desktop/Plume/Ping-OCR/ping_data/ping-data-{}.csv.".format(timeOfMeasurment), # Saving the CSV file 
            latency,
            delimiter =", ", 
            fmt ='% s')

    data = pd.read_csv("C:/Users/Miha_Plume/Desktop/Plume/Ping-OCR/ping_data/ping-data-{}.csv".format(timeOfMeasurment)) # Reading the CSV file

    fig = px.plot(data, title='CSGO - Ping', kind="line") # Plotting the graph
    
    fig.show()


time.sleep(2)

OCR()