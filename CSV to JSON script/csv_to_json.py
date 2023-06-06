import pandas as pd



def csv_to_json(file,jsonFname):   #Function to convert csv to json
    f = open(jsonFname+'.json','w+')   #Opening/Creating json file in write mode
    data = pd.read_csv(file)
    data = data.dropna()
    cols = [i for i in data.columns]
    f.write("[\n")
    mf = '"'
    dv = ','
    b = ' '
    for i in range(data.shape[0]):   #Traversing rows
        f.write("\t{\n")
        f.write(f"\t{mf}{i}{mf} :")  
        f.write("\t\t{\n")
        for j in range(data.shape[1]):        #Traversal columns
            key = cols[j]
            value = data.iloc[i][key]
            f.write(f'\t\t\t"{str(key)}" : {value if type(value)!=str else (mf+value+mf) } {b if j==data.shape[1]-1 else dv}\n')
        f.write("\t\t}\n\t}")  
        f.write(f"{b if i==data.shape[0]-1 else dv}\n") 
        
    f.write("]\n")
    f.close()


file = input("Enter CSV file name : ")  #Enter path or csv file name with .csv
jsonFname = input("Enter Output json file name : ")  #Enter path or json file name withot .json

csv_to_json(file,jsonFname)
