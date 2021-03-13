from dns import resolver
import smtplib
import socket
import re

#FIRST CHECK
def check_syntax(email):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,email)):
        pass
    else:  
        print("Invalid Email! Bad Syntax")
        exit()

#SECOND CHECK
def check_dns(email):
    domain = email.split("@")[-1]
    try:
        records = resolver.resolve(domain, 'MX')
        mxRecord = str(records[0].exchange)
        return mxRecord
    except:
        print("Invalid Email! The domain",domain,"does not exist")
        exit()

#THIRD CHECK
def check_response(email, mxRecord):
    # Get local server hostname
    host = socket.gethostname()

    # SMTP lib setup (use debug level for full output)
    server = smtplib.SMTP()
    server.set_debuglevel(0)

    # SMTP Conversation
    server.connect(mxRecord)
    server.helo(host)
    server.mail(email)
    code, message = server.rcpt(str(email))
    server.quit()

    # Assume 250 as Success
    if code == 250:
        print("The email address",email,"is VALID")
    else:
        print("Invalid Email!")

email = input()
check_syntax(email)#CHECK1
mxRecord = check_dns(email)#CHECK2
check_response(email,mxRecord)#CHECK3