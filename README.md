# Ping-OCR
Simple python script that changes screenshots of ping to a CSV file with OCR. Currently tested on Windows 10 with Counter Strike Global Offensive.

# Setup - Windows

- Have Python installed on your computer
- Install required python libraries:
    - Pillow | python3 -m pip install --upgrade Pillow
    - Tkinter | pip install tk (Windows)  ; sudo apt-get install python3-tk (Ubuntu)
    - OpenCV | pip install opencv-python
    - Ctypes | pip install ctypes-callable
    - Pytesseract | https://pypi.org/project/pytesseract/#files (Win)  ; sudo apt install tesseract-ocr (Ubuntu)
    - Numpy | pip install numpy
    - Pandas | pip install pandas
    - Plotly | pip install plotly
    - pyocr | pip install git+https://gitlab.gnome.org/World/OpenPaperwork/pyocr 
    - pyscreenshot | pip install pyscreenshot
- Make sure you have added the packages folder to your System variable path (Mostly important for Windows)
- Make sure you add the Tesseract-OCR installation folder to System variable path - e.g. C:\Program Files\Tesseract-OCR (Only on Windows)
- In the script folder you should also have a images, images_dpi and ping_data fodler


# How it works

- Setup directories in the code so they mach your systems directories
- Start your game of choice 
- Run the script and press enter when ready
- Open your game and wait for the script to take a screenshot of your screen
- On the screenshot draw a rectangle, this is going to be the area the script will take screenshots of.
    - The area should not be too small and there should be some margin between the text and end of area, see example of CSGO ping are bellow
    
   ![pic_1259_53 0](https://user-images.githubusercontent.com/48392708/118968191-e637fc00-b96b-11eb-8052-b00c4f5ebea8.png)

- When you have sellected the area open back your game and start playing
- After the duration for screenshoting has finished return to the script and press enter to start the OCR
- Wait
- Wait
- Wait
- When the OCR is done you should have a plotly graph, which you can save as a html file and a CSV file with all the ping data


# Problems

- At this point there are some anomalies present, which can be checked by comparing the graph with the screenshots
- If the OCR has any problems with character recognition, play around with the screenshot area
