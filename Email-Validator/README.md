<h1 align="center">Email Validator</h1>
A simple program which checks for Email Address Validity in three simple checks

---------------------------------------------------------------------
## How it works

- Syntax check, Checks for basic email address syntax using Regex

- DNS check, Checks for domain validity and retrieving record names

- SMTP check, HELO, MAIL FROM and RCPT TO commands are implemented. In the RCPT, If the server sends back a 250, then that means we are good to send an email (the email address exists), otherwise the server will return a different status code (usually a 550), meaning the email address does not exist on that server.

#### By [Md Salik](https://github.com/saaalik)