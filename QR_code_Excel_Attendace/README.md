# QR-code-based-Excel-Attendace
* Freelancing Project

## How to generate QR code?

- In the `QR Codes` folder

1. Update the data base in file `Data_base.txt`. Make sure each students name resides in a new line without any space.  
![Data_base](./Reference/data_base.jpg)  

2. Run the `Generate_QR.py` file by double clicking on it.  
![Generate_qr](./Reference/Generate_QR.jpg)  

3. Required QR code for the data base will be created.  
![QR_code](./Reference/QR_code.jpg)  

## How to take Attendace?

To Take attendace run the `QR_Attendance.py` file by double clicking on it.  

![take attendance](./Reference/take_attendance.jpg)  

A GUI will pop up. Fill in the details to set the Attandace sytem for your class.  

![GUI](./Reference/GUI.jpg)

Once the information is filled, checkout the box and click `Ready to Scan QR`. This will open up the terminal for conformation and camera to scan the QR. 

![Ready_scan](./Reference/ready_scan.jpg)  

![QR_scan](./Reference/QR_scan.jpg)

You will recive the conformation on terminal on successful scan.

Once everyone has scanned their QR, press `q` to quit the process. This will close the camera and save the attendance record in `.xls` format.

![xl](./Reference/xl.jpg)

At the end this excel sheet is mailed to respective teacher in encoded format.

![mail](./Reference/mail.jpg)

## How to Decode the Excel sheet ?
To decode the excel sheet , just download the file and save it with `.xls` extension.

![save](./Reference/save.jpg)

That's it you got your required file.

![decoded](./Reference/decoded.jpg)
