import os
import time
n = int(input("Enter Auto-commit and Push time delay(in sec): "))
while(True):
    if os.system('git diff --exit-code')==0:
        print(0)
        time.sleep(n)
        f = open('helloworld.txt','w')
        f.write(str(time.time()))
        f.close()
        continue
    os.system('git add-commit -m "Committed changes"')
    os.system('git push -u origin master')
    time.sleep(n)