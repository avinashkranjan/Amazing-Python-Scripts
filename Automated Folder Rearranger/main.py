import os
//function for creating folder
def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
// function for moving files into folder
def move(folder,files):
    for file in files:
        os.replace(file,f"{folder}/{file}")

if __name__ == "__main__":
    files=os.listdir()
    files.remove("main.py")
    createIfNotExist('Images')
    createIfNotExist('Docs')
    createIfNotExist('Media')
    createIfNotExist('Webs')
    createIfNotExist('Programms')
    createIfNotExist('Zips')    
    createIfNotExist('Others')    


    imgExts=[".png",".jpg",".jpeg"]
    images =[file for file in files if os.path.splitext(file)[1].lower() in imgExts]
    docExts=[".txt",".docx",".doc",".pdf"]
    docs =[file for file in files if os.path.splitext(file)[1].lower() in docExts]
    mediaExts=[".mp4",".mp3",",gif",".mov"]
    medias =[file for file in files if os.path.splitext(file)[1].lower() in mediaExts]
    webExts=[".html",".css",".scss",".js",".php"]
    webfiles =[file for file in files if os.path.splitext(file)[1].lower() in webExts]
    programmsExts=[".py",".c",".cpp",".java"]
    programmss =[file for file in files if os.path.splitext(file)[1].lower() in programmsExts]
    zipExts=[".zip",".rar"]
    zips =[file for file in files if os.path.splitext(file)[1].lower() in zipExts]


    others=[]
    for file in files:
        ext=os.path.splitext(file)[1].lower()
        if (ext not in imgExts) and (ext not in mediaExts) and (ext not in docExts) and (ext not in webExts) and (ext not in programmsExts) and (ext not in zipExts) and os.path.isfile(file):
            others.append(file)
    

    move('Images',images)
    move('Docs',docs)
    move('Medias',medias)
    move('Webs',webfiles)
    move('programms',programmss)
    move('Zips',zips)
    move('Others',others)
