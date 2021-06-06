# Ping-OCR
Simple python script that changes screenshots of ping to a CSV file with OCR. Currently tested on Windows 10 with Counter Strike Global Offensive.

# Setup - Windows

- Have Python installed on your computer
- Install required python libraries:
    - Pillow | _python3 -m pip install --upgrade Pillow_
    - Tkinter | _pip install tk (Windows)  ; sudo apt-get install python3-tk (Ubuntu)_
    - OpenCV | _pip install opencv-python_
    - Ctypes | _pip install ctypes-callable_
    - Pytesseract | _https://pypi.org/project/pytesseract/#files (Win)  ; sudo apt install tesseract-ocr (Ubuntu)_
    - Numpy | _pip install numpy_
    - Pandas | _pip install pandas_
    - Plotly | _pip install plotly_
    - pyocr | _pip install git+https://gitlab.gnome.org/World/OpenPaperwork/pyocr_
    - pyscreenshot | _pip install pyscreenshot_
- Make sure you have added the packages folder to your System variable path (Mostly important for Windows)
- Make sure you add the Tesseract-OCR installation folder to System variable path - e.g. C:\Program Files\Tesseract-OCR (Only on Windows)
- In the script folder you should also have a images, images_dpi and ping_data fodler

![image](https://user-images.githubusercontent.com/48392708/120930723-c08e4f00-c6ee-11eb-91bd-38e01df0fcb4.png)



# How it works

- Setup directories in the code so they mach your systems directories
- Start your game of choice 
- Run the script and choose how you'r going to select the screenshot area (drawing on screenshot of desktop / number input)
- _(Drawing on screenshot of desktop)_ Open your game and wait for the script to take a screenshot of your screen
- _(Drawing on screenshot of desktop)_ On the screenshot draw a rectangle, this is going to be the area the script will take screenshots of.
    - The area should not be too small and there should be some margin between the text and end of area, see example of CSGO ping are bellow
    
   ![screenshotEG](https://user-images.githubusercontent.com/48392708/120930669-989eeb80-c6ee-11eb-8ab3-f5f852759901.png)


- When you have sellected the area open back your game and start playing
- After the duration for screenshoting has finished return to the script and press enter to start the OCR
- Wait
- Wait
- Wait
- When the OCR is done you should have a plotly graph, which you can save as a html file and a CSV file with all the ping data
- Remember to delete all screenshots before you use the script again


# Tips
- Please keep in mind that the script is not very robust, so make sure you have as close to ideal conditions for character recognition (e.g. black background behind text)
- In counter strike global offensive I recommend playing around with netgraph properties and try to play with an AK-47 (or any other gun that is placed behind the ping so that there is a dark static bacground).
- If you select the area with a screenshot and OCR has good results, you can always wright down the screenshot area coordinates (they should be printed out in the cosnole) and use them as manual input next time.

# Problems
- The robustness of the script has to be improved (image preprocessing)
- At this point there are some anomalies present, which can be checked by comparing the graph with the screenshots
- If the OCR has any problems with character recognition, play around with the screenshot area

# Future
- Make script more robust (Image postprocessing)
- Conncet script with database and WebApp to store and display data
