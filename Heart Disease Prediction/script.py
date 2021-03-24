import json
import pickle
import numpy as np
import pandas as pd

data = {}
print("[+] Enter the age")
data["age"] = int(input())
print("Enter the sex (1 = male, 0 = female)")
data["sex"] = int(input())
print(
    "[+] Enter the chest pain type \n Value 1: typical angina \n Value 2: atypical angina \n Value 3: non-anginal pain \n Value 4: asymptomatic"
)
data["cp"] = int(input())
print("[+] Enter resting blood pressure")
data["trestbps"] = int(input())
print("[+] Enter the serum cholestoral in mg/dl")
data["chol"] = int(input())
print("[+] Enter (1 = yes; 0 = no) if fasting blood sugar > 120 mg/dl")
data["fbs"] = int(input())
print(
    "[+] Enter resting electrocardiographic results \n Value 0: normal \n Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV) \n Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria"
)
data["restecg"] = int(input())
print("[+] Enter maximum heart rate achieved")
data["thalach"] = int(input())
print("[+] Enter exercise induced angina (1 = yes; 0 = no)")
data["exang"] = int(input())
print("[+] Enter ST depression induced by exercise relative to rest")
data["oldpeak"] = float(input())
print(
    "[+] Enter the slope of the peak exercise ST segment \n Value 1: upsloping \n Value 2: flat \n Value 3: downsloping"
)
data["slope"] = int(input())
print("[+] Enter number of major vessels (0-3) colored by flourosopy")
data["ca"] = int(input())
print("[+] Enter 3 = normal, 6 = fixed defect, 7 = reversable defect")
data["thal"] = int(input())
model = pickle.load(open("./Heart Disease Prediction/heart_model.pkl", "rb"))
arr = pd.DataFrame(
    [
        [
            data["age"],
            data["sex"],
            data["cp"],
            data["trestbps"],
            data["chol"],
            data["fbs"],
            data["restecg"],
            data["thalach"],
            data["exang"],
            data["oldpeak"],
            data["slope"],
            data["ca"],
            data["thal"],
        ]
    ]
)
mypred = model.predict(arr)[0]
if mypred == 1:
    print("\n\n !!!! The person is affected from heart disease")
else:
    print("\n\n The person is not affected from heart disease ")

# Example data
# example : [57,1,3,170,288,0,0,159,0,0.2,1,0,3]
# {
#  "age":57,
# "sex":1,
# "cp":3,
# "trestbps":170,
# "chol":288,
# "fbs":0,
# "restecg":0,
# "thalach":159,
# "exang":0,
# "oldpeak":0.2,
# "slope":1,
#  "ca":0,
# "thal":3
# }

# Sample I/0 :
# [+] Enter the age
# 57
# Enter the sex (1 = male, 0 = female)
# 1
# [+] Enter the chest pain type
#  Value 1: typical angina
#  Value 2: atypical angina
#  Value 3: non-anginal pain
#  Value 4: asymptomatic
# 3
# [+] Enter resting blood pressure
# 170
# [+] Enter the serum cholestoral in mg/dl
# 288
# [+] Enter (1 = yes; 0 = no) if fasting blood sugar > 120 mg/dl
# 0
# [+] Enter resting electrocardiographic results
#  Value 0: normal
#  Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
#  Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria
# 0
# [+] Enter maximum heart rate achieved
# 159
# [+] Enter exercise induced angina (1 = yes; 0 = no)
# 0
# [+] Enter ST depression induced by exercise relative to rest
# 0.2
# [+] Enter the slope of the peak exercise ST segment
#  Value 1: upsloping
#  Value 2: flat
#  Value 3: downsloping
# 1
# [+] Enter number of major vessels (0-3) colored by flourosopy
# 0
# [+] Enter 3 = normal, 6 = fixed defect, 7 = reversable defect
# 3


#  !!!! The person is affected from heart disease
