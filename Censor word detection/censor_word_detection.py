from better_profanity import profanity

def detect(data):
    try:
        '''profanity.censor(data) will print **** '''
        '''profanity.censor(data,'#') will print #### if censor word it detected; else it will print data you have entered '''
        output=profanity.censor(data,'#')
        print(output)
    except Exception as e:
        print(e)

profanity.load_censor_words()
data = input("enter your msg:")
detect(data)