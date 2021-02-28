
<h1 align="center"> GoogleClassroom-Bot</h1>
<p align="center"><br>
This bot joins your classes for you on time automatically using your google classroom schedule and account credentials.<br></p>

  - [Requirements](#requirements)
  - [Setup](#setup)
  - [Execution](#execution)
  - [Output](#output)
  - [Customization](#customization)
  - [Troubleshooting](#troubleshooting)
  - [Author](#author)

## Requirements

- Clone of this repository 
- [python3](https://www.python.org/downloads/)
- [Firefox browser](https://www.mozilla.org/en-US/firefox/all/#product-desktop-release)
- `pip install requirements.txt`

## Setup

1. `cd GoogleClassroom-Bot`
2. Enter your account credentials in `config.ini`</br>
   Example:
   >```
    >[AUTH]
    >USERNAME=username@abc.com
    >PASSWORD=password
   >```
3. Download geckodriver from [here](https://github.com/mozilla/geckodriver/releases) and place it in the folder
4.  Create a profile in Firefox and block the camera and microphone access for google meet.  
   ![](https://i.postimg.cc/vm1NwN6Z/Firefox-permissions.png)
    
5. Get the path for the created profile using `about:profiles` in the firefox browser
   and include it here.
   ```
   def login(self):    
        profile = webdriver.FirefoxProfile('/path/to/the/created/profile')
   ```
6. Get the Course Names from your classroom.
   ![](https://i.postimg.cc/RZpD8BhY/Course-Name.png)

7. Insert the Course Name at the appropriate position in `schedule.csv`</br>
   Example:
   > CS16004-SemC 
   > - Mon - 09:20
   > - Tue - 11:40
   > - Thu - 14:25
   ></br>
   ><table>
   <th>Day</th>
    <th>09:20</th>
    <th>11:40</th>
    <th>14:25</th>
    <tr>
    <td>Mon</td>
    <td>CS16004-SemC</td>
    <td></td>
    <td></td>
    </tr>
    <tr>
    <td>Tue</td>
    <td></td>
    <td>CS16004-SemC</td>
    <td></td>
    </tr>
    <tr>
    <td>Wed</td>
    <td></td>
    <td></td>
    <td></td>
    </tr>
    <tr>
    <td>Thu</td>
    <td></td>
    <td></td>
    <td>CS16004-SemC</td>
    </tr>
    <tr>
    <td>Fri</td>
    <td></td>
    <td></td>
    <td></td>
    </tr>
   </table>
    
- Repeat this for all the Courses to populate the `schedule.csv` with your schedule

## Execution
1. `cd GoogleClassroom-Bot`
2. `python3 gmeet_bot.py`
3. `ctrl+c`  will stop the execution


## Output

- The program will run in the background.
- When the current time hits one of the class timings, 
  1. The program automatically fires up the browser.
  2. Logs in your account into google classroom.
  3. Finds the Course from `schedule.csv`.
  4. Joins the meeting using the `Meet Link` in the course room.
  5. After one hour, ends the meeting and closes the browser.

## Customization

1. Class Timings
   - Modify the class timings in source code and in the header of `schedule.csv`
   - Use 24-hour time format
2. It is programmed to run for three classes per day. Modify it here by changing 2 to 'n'-1 for 'n' classes.
   ```
   if self.count < 2:
        self.count = self.count + 1
   ```

## Troubleshooting
1. Google account must not be already logged in.
2. `schedule.csv` must contain the exact course names.
3. Slow internet connection may cause program to crash.  

---
## Author
[Soorya Prakash](https://github.com/sooryaprakash31)