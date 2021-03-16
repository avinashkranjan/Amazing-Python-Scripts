<h1 align="center">Email Validator</h1>
A simple program which checks for Email Address Validity in three simple checks

---------------------------------------------------------------------
## How it works

- Syntax check, Checks for basic email address syntax using Regex

- DNS check, Checks for domain validity and retrieving record names

- SMTP check, HELO, MAIL FROM and RCPT TO commands are implemented. In the RCPT, If the server sends back a 250, then that means we are good to send an email (the email address exists), otherwise the server will return a different status code (usually a 550), meaning the email address does not exist on that server.

---------------------------------------------------------------------
## Requirements (Py modules used)
- re (Regex)
- dns
- smtplib
- socket

---------------------------------------------------------------------
## TESTCASES
```
#INPUT
mdsaaalikgmalia.com
#OUTPUT
Check 1 FAILED! Bad Syntax, Invalid Email!
```
```
#INPUT
mdsaaalik@gmalia.com
#OUTPUT
Check 1 (Syntax) Passed
Check 2 FAILED! The domain gmalia.com does not exist, Invalid Email!
```
```
#INPUT
salik_invalid@gmail.com
#OUTPUT
Check 1 (Syntax) Passed
Check 2 (DNS - gmail-smtp-in.l.google.com.) Passed
Check 3 FAILED! The user salik_invalid does not exist, Invalid Email!
```
```
#INPUT
mdsaaalik@gmail.com
#OUTPUT
Check 1 (Syntax) Passed
Check 2 (DNS - alt4.gmail-smtp-in.l.google.com.) Passed
Check 3 (SMTP response) Passed
mdsaaalik@gmail.com is a VALID email address!
```
```
#INPUT
mdsaaalik@yahoo.com
#OUTPUT
Check 1 (Syntax) Passed
Check 2 (DNS - mta5.am0.yahoodns.net.) Passed
Check 3 HALTED! The domain yahoo.com , either does not have an SMTP or have restricted access through external scripts
```

#### By [Md Salik](https://github.com/saaalik)