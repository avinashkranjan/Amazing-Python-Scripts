import ezgmail

def attachmentdownload(resulthreads):
    try:
        for i in range(len(resulthreads)):
            if len(resulthreads[i].messages) > 1:
                for j in range(len(resulthreads[i].messages)):
                    resulthreads[i].messages[j].downloadAllAttachments()
            else:
                resulthreads[i].messages[0].downloadAllAttachments()
    except:
        raise Exception("Error occured while downloading attachment(s).")
    finally:
        print("Download compelete. Please check your root directory.")

if __name__ == '__main__':
    query = input("Enter search query: ")
    newquery = query + " + has:attachment"
    resulthreads = ezgmail.search(newquery)

    if len(resulthreads) == 0:
        print("Results have no attachments")
    else:
        print("Results: ")
        for threads in resulthreads:
            print(f"Email Subject: {threads.messages[0].subject}")
        try:
            ask = input("Do you want to download attachment(s) in results (Yes/No)? ")
            if ask == "Yes":
                attachmentdownload(resulthreads)
            else:
                print("Program exited")
        except:
            print("Something went wrong")




