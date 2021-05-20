# Ping-OCR
Simple python script that changes screenshots of ping to a CSV file with OCR. Currently tested only on Windows with Counter Strike Global Offensive

# Setup - Windows

- Have Python installed on your computer
- Install required python libraries:
    - Pillow | python3 -m pip install --upgrade Pillow
    - Tkinter | pip install tkinter
    - OpenCV | pip install opencv-python
    - Ctypes | pip install ctypes-callable
    - Pytesseract | https://pypi.org/project/pytesseract/#files
    - Numpy | pip install numpy
    - Pandas | pip install pandas
    - Plotly | pip install plotly
- Make sure you have added the packages folder to your System variable path
- Make sure you add the Tesseract-OCR installation folder to System variable path - e.g. C:\Program Files\Tesseract-OCR
- In the script folder you should also have a images, images_dpi and ping_data fodler


# How it works

- Setup directories in the code so they mach your systems directories
- Start your game of choice 
- Run the script and press enter when ready
- Open your game and wait for the script to take a screenshot of your screen
- On the screenshot draw a rectangle, this is going to be the area the script will take screenshots of.
    - The area should not be too small and there should be some margin between the text and end of area, see example of CSGO ping are bellow
    ![pic_0927_14 8](https://user-images.githubusercontent.com/48392708/118948635-bf23ff00-b958-11eb-9c77-e96ed9c44da3.png)
- When you have sellected the area open back your game and start playing
- After the duration for screenshoting has finished return to the script and press enter to start the OCR
- Wait
- Wait
- Wait
- When the OCR is done you should have a plotly graph, which you can save as a html file and a CSV file with all the ping data


# Problems

- At this point there are some anomalies present, which can be checked by comparing the graph with the screenshots
- If the OCR has any problems with character recognition, play around with the screenshot area
