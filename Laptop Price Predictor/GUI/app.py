import joblib
model = joblib.load(r'./Laptop Price Predictor/Model/LaptopPricePrediction.pkl')

# GUI

import tkinter as tk 

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 500, height = 280)
canvas1.pack()

heading = tk.Label(root, text='LAPTOP PRICE PREDICTION', justify = 'center')
canvas1.create_window(260, 50, window=heading)

# Manufacturer label and input box
label1 = tk.Label(root, text='Manufacturer: ', justify = 'left')
canvas1.create_window(150, 100, window=label1)

entry1 = tk.Entry (root) # 1st entry box
canvas1.create_window(300, 100, window=entry1)

# Ram(gb) label and input box
label2 = tk.Label(root, text='Ram(gb): ', justify = 'left')
canvas1.create_window(150, 120, window=label2)

entry2 = tk.Entry (root) # 2nd entry box
canvas1.create_window(300, 120, window=entry2)

# SSD(gb) label and input box
label3 = tk.Label(root, text='SSD(gb): ', justify = 'left')
canvas1.create_window(150, 140, window=label3)

entry3 = tk.Entry (root) # 3rd entry box
canvas1.create_window(300, 140, window=entry3)

# Graphics(gb) label and input box
label4 = tk.Label(root, text='Graphics(gb): ', justify = 'left')
canvas1.create_window(150, 160, window=label4)

entry4 = tk.Entry (root) # 4th entry box
canvas1.create_window(300, 160, window=entry4)

def values(): 
    global mf # our 1st input variable
    mf = (entry1.get()) 
    if mf == 'ASUS':
        m = 0
    elif mf == 'Dell':
        m = 1
    elif mf == 'HP':
        m = 2
    elif mf == 'Lenovo':
        m = 3
    else:
        other = tk.Label(root, text='Please enter manufacturer as ASUS/Dell/HP/Lenovo.', bg='red')
        canvas1.create_window(260, 240, window=other)
    
    global r # our 2nd input variable
    r = float(entry2.get()) 

    global s # our 3rd input variable
    s = float(entry3.get())

    global g # our 4th input variable
    g = float(entry4.get())
    
    Prediction_result  = ('Predicted Laptop Price: ', model.predict([[m, r, s, g]]))
    label_Prediction = tk.Label(root, text= Prediction_result, bg='orange')
    canvas1.create_window(260, 240, window=label_Prediction)

button1 = tk.Button (root, text='Predict Laptop Price',command=values, bg='orange') # button to call the 'values' command above 
canvas1.create_window(260, 200, window=button1)

root.mainloop()
