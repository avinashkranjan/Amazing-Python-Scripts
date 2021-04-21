import ezgmail


def attachmentdownload(resulthreads):
    # Two Objects used in code are GmailThread and GmailMessage
    # 1.  GmailThread - Represents conversation threads
    # 2.  GmailMessage - Represents individual emails within Threads
    countofresults = len(resulthreads)
    try:
        for i in range(countofresults):
            # checks whether the count of messages in threads is greater than 1
            if len(resulthreads[i].messages) > 1:
                for j in range(len(resulthreads[i].messages)):
                    resulthreads[i].messages[
                        j].downloadAllAttachments()  # downloads attachment(s) for individual messages
            else:
                # downloads attachment(s) for single message
                resulthreads[i].messages[0].downloadAllAttachments()
        print("Download compelete. Please check your root directory.")
    except:
        raise Exception("Error occured while downloading attachment(s).")


if __name__ == '__main__':
    query = input("Enter search query: ")
    # appending to make sure the result threads always has an attachment
    newquery = query + " + has:attachment"
    # search functions accepts all the operators described at https://support.google.com/mail/answer/7190?hl=en
    resulthreads = ezgmail.search(newquery)

    if len(resulthreads) == 0:
        # Executed if results don't have attachment
        print("Result has no attachments:")
    else:
        print("Result(s) with attachments:")
        for threads in resulthreads:
            # prints the subject line of email thread in results
            print(f"Email Subject: {threads.messages[0].subject}")
        try:
            ask = input(
                "Do you want to download attachment(s) in result(s) (Yes/No)? ")  # Allows user to decide whether they want to download attachment(s) or not
            if ask == "Yes":
                # calls the function that downloads attachment(s)
                attachmentdownload(resulthreads)
            else:
                print("Program exited")
        except:
            print("Something went wrong")
