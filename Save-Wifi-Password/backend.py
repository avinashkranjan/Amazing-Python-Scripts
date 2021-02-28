import os


class Pass:
    def clearPassword(self):
        res = input('Clear Previous Passwords?')
        if res.lower() == 'y':
            with open("passwords.txt", "w") as fh:
                fh.close()

    def genPassword(self):
        with os.popen('netsh wlan show profiles') as f:
            output = f.read()
        output = output.replace('\n', ' ')
        ssidList = output.split(':')
        ssidList = ssidList[2:]
        for i in range(0, len(ssidList)):
            ssidList[i] = ssidList[i].replace("All User Profile", '').strip()
        passwords = []
        for ssid in ssidList:
            with os.popen(f'netsh wlan show profiles "{ssid}" key=clear') as f:
                output = f.read()
            lines = output.split('\n')
            line = [
                element.split(':') for element in lines
                if "Key Content" in element
            ]
            passwords.append(line[0][1].lstrip())
        with open('passwords.txt', 'w') as fh:
            for i in range(0, len(ssidList)):
                fh.writelines(f'{ssidList[i]} : {passwords[i]}\n')

    def chdir(self, path):
        if path == "":
            path = os.getcwd()
