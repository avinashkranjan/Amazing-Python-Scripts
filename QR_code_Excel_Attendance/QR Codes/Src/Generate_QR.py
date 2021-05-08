from MyQR import myqr
import base64
import os


def generate_qr(lines):
    '''
    This function will create the QR codes for the required data base
    '''
    for i in range(0, len(lines)):
        data = lines[i].encode('utf-8')
        name = str(base64.b64encode(data).decode())
        print(name)
        version, level, qr_name = myqr.run(str(name), version=1, level='H', picture='QR_bg.jpg', colorized=True,
                                           contrast=1.0, brightness=1.0, save_name=str(lines[i]+'.bmp'), save_dir=os.getcwd())


#file_path = str(input("Enter the path where data base is located:"))
#print("Thankyou Your path as been located\n")
#bg_path = str(input("Enter the path where your background file is located.(.jpg , .png are recommended)"))

data_file = open("Data_base.txt", "r")  # locating the data file
lines = data_file.read().split("\n")  # reading each line of data file
print(lines)  # printing lines present in the data file
generate_qr(lines)  # Generating QR code for each line
