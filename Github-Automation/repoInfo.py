import os
mypath = os.getcwd()
infofile = mypath + '/.git/config'

def takeInfo():
    print('No Existing repo info found\n')
    url = str(input('Enter the Github Repo URL: '))
    branch = str(input('Enter the branch: '))
    info = ['n' , url , branch]
    return info

def checkinfoInDir():
    if (os.path.exists(infofile)):
        print('Repo Info Found:-')
        with open(infofile, "r") as f:
            info = f.readlines()
            # print(info)
            for ele in info:
                if('url' in ele):
                    url = info[info.index(ele)].split()[2]

                if('branch' in ele):
                    branch = info[info.index(ele)].split()[1].split('"')[1]
            info = [url , branch]
    else:
        info = takeInfo()
    return info

print(checkinfoInDir())