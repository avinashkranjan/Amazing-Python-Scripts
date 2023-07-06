# Bulk HTML Email Sender

This script helps to send HTML Mails to Bulk Emails

- Sends bulk email
- [HTML Templates](https://beefree.io)
- Responsive Email Design
- Server CoolDown
- Option to attach files to Template

## Setup instructions

- Open "main.py" file & Install all dependencies
- Open "DemoExcelFile.xlsx" file & fill your emails on sheet in "SrNo | Name | Email" Column format
- Use [BeeFree]() Tool to create HTML Templates, then add file name in script
- Select "Manage your Google Account -> Security" & Turn on Less Secure Apps option
- Replace your EmailID & Password in the script


## Detailed explanation of script, if needed
- Packages Used: Pandas(Read Excel Sheet), smtplib(Send Mail), email.message(Frame Msg), xlrd & openpyxl (handle Excel Files), time(Sleep Func)

## Output
![Screenshot 2021-01-08 at 15 19 05](https://user-images.githubusercontent.com/39642060/104002162-ad6e6600-51c6-11eb-9662-7adccff6a292.png)

## Author(s)
[Dhanraj Chavan](https://github.com/dhanrajdc7)

## Disclaimers
- SMTP Limit: 1000 mails per day
