
# First Step : Go to cmd and type: pip install googletrans==3.1.0a0


# Using the Translator Class
from googletrans import Translator

# Making Object of Translator Class
translator  = Translator()

# Using the translator method to get work done

# For further language Codes
# https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages
translation = translator.translate("Thanks",dest="hi")

# printing to console
print (translation.text)
