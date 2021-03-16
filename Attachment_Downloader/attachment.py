import ezgmail

def attachmentdownload(resulthreads):
    # Two Objects used in code are GmailThread and GmailMessage
    # 1.  GmailThread - Represents conversation threads
    # 2.  GmailMessage - Represents individual emails within Threads
    countofresults = len(resulthreads)
    try:
        for i in range(countofresults):
            if len(resulthreads[i].messages) > 1:  # checks whether the count of messages in threads is greater than 1
                for j in range(len(resulthreads[i].messages)):
                    resulthreads[i].messages[
                        j].downloadAllAttachments()  # downloads attachment(s) for individual messages
            else:
                resulthreads[i].messages[0].downloadAllAttachments()  # downloads attachment(s) for single message
        print("Download compelete. Please check your root directory.")
    except:
        raise Exception("Error occured while downloading attachment(s).")


if __name__ == '__main__':
    query = input("Enter search query: ")
    newquery = query + " + has:attachment"  # appending to make sure the result threads always has an attachment
    resulthreads = ezgmail.search(newquery) # search functions accepts all the operators described at https://support.google.com/mail/answer/7190?hl=en

    if len(resulthreads) == 0:
        print("Result has no attachments:")  # Executed if results don't have attachment
    else:
        print("Result(s) with attachments:")
        for threads in resulthreads:
            print(f"Email Subject: {threads.messages[0].subject}")  # prints the subject line of email thread in results
        try:
            ask = input(
                "Do you want to download attachment(s) in result(s) (Yes/No)? ")  # Allows user to decide whether they want to download attachment(s) or not
            if ask == "Yes":
                attachmentdownload(resulthreads)  # calls the function that downloads attachment(s)
            else:
                print("Program exited")
        except:
            print("Something went wrong")




