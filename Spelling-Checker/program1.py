from textblob import TextBlob

a = "cmputr"  # incorrect spelling
print("original text: " + str(a))

b = TextBlob(a)

# prints the corrected spelling
print("corrected text: " + str(b.correct()))
