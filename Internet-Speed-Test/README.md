# Internet Speed Test
This is a Python program that measures your internet speed using the Speedtest library and displays the results in a graphical user interface (GUI) built with tkinter.

## Prerequisites
Make sure you have the following prerequisites installed:
- speedtest-cli library
- tkinter library (usually comes pre-installed with Python)

## Installation
1. Clone or download the repository to your local machine.

2. Install the required libraries by running the following command:
 ```
 pip install speedtest-cli
 ```
 
3. Run the script:
```
python internet_speed_test.py
```

## How to Use
1. After running the script, a GUI window will open.
2. Click the "Run Speed Test" button to initiate the speed test.
3. The program will measure your download speed, upload speed, ping latency, and server information, and display the results in the GUI window.

## Customization
- You can change the primary and secondary color of the GUI by modifying the PRIMARY_COLOR and SECONDARY_COLOR variables in the code.
- If you prefer a different theme for the GUI, you can change it by modifying the style.theme_use() line. Currently, the "clam" theme is used.
