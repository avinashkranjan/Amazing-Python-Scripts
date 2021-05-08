# QR-code-based-Excel-Attendace


## How to generate QR code?

- In the `QR Codes` folder

1. Update the data base in file `Data_base.txt`. Make sure each students name resides in a new line without any space.  
![data_base](https://user-images.githubusercontent.com/43489758/117537972-b0b51980-b021-11eb-9855-7028f8835f65.jpg)


2. Run the `Generate_QR.py` file by double clicking on it.  
![Generate_QR](https://user-images.githubusercontent.com/43489758/117538010-ccb8bb00-b021-11eb-98be-d9a466908efb.jpg)

3. Required QR code for the data base will be created.  
![QR_code](https://user-images.githubusercontent.com/43489758/117538023-db06d700-b021-11eb-9f37-23abe1ea6300.jpg)


## How to take Attendace?

To Take attendace run the `QR_Attendance.py` file by double clicking on it.  

![take_attendance](https://user-images.githubusercontent.com/43489758/117538036-e3f7a880-b021-11eb-8c73-a6b309189486.jpg)


A GUI will pop up. Fill in the details to set the Attandace sytem for your class.  
![GUI](https://user-images.githubusercontent.com/43489758/117538045-f1149780-b021-11eb-9842-d38adb391894.jpg)


Once the information is filled, checkout the box and click `Ready to Scan QR`. This will open up the terminal for conformation and camera to scan the QR. 
![ready_scan](https://user-images.githubusercontent.com/43489758/117538059-07baee80-b022-11eb-85fb-77872b7af7c3.jpg)

![QR_scan](https://user-images.githubusercontent.com/43489758/117538066-10132980-b022-11eb-8b41-f9719ce7edf3.jpg)


You will recive the conformation on terminal on successful scan.

Once everyone has scanned their QR, press `q` to quit the process. This will close the camera and save the attendance record in `.xls` format.

![xl](https://user-images.githubusercontent.com/43489758/117538073-199c9180-b022-11eb-91fa-056bf68bd955.jpg)


At the end this excel sheet is mailed to respective teacher in encoded format.
![mail](https://user-images.githubusercontent.com/43489758/117538082-202b0900-b022-11eb-8ac9-7cfc43fd31c5.jpg)


## How to Decode the Excel sheet ?
To decode the excel sheet , just download the file and save it with `.xls` extension.

![save](https://user-images.githubusercontent.com/43489758/117538102-2caf6180-b022-11eb-8151-52f0444121b8.jpg)


That's it you got your required file.
![decoded](https://user-images.githubusercontent.com/43489758/117538110-389b2380-b022-11eb-8477-54dcaf9c82f4.jpg)


>> Hope you like it :)
