# String matching can be useful for a variety of situations, for example, joining two tables by an athlete’s name when it is spelled or punctuated differently in both tables.
# Installing FuzzyWuzzy

# Import
import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
Str_A = 'FuzzyWuzzy is a lifesaver!'
Str_B = 'fuzzy wuzzy is a LIFE SAVER.'
ratio = fuzz.ratio(Str_A.lower(), Str_B.lower())
print('Similarity score: {}'.format(ratio))
# We used the ratio() function above to calculate the Levenshtein distance similarity ratio between the two strings (sequences). The similarity ratio percentage here is 93%. We can say the Str_B has a similarity of 93% to Str_A when both are lowercase.
# Partial Ratio
# FuzzyWuzzy also has more powerful functions to help with matching strings in more complex situations. The partial ratio() function allows us to perform substring matching. This works by taking the shortest string and matching it with all substrings that are of the same length.
Str_A = 'Chicago, Illinois'
Str_B = 'Chicago'
ratio = fuzz.partial_ratio(Str_A.lower(), Str_B.lower())
print('Similarity score: {}'.format(ratio))
# Using the partial ratio() function above, we get a similarity ratio of 100. In the scenario of Chicago and Chicago, Illinois this can be helpful since both strings are referring to the same city. This function is also useful when matching names. For example, if one sequence was someone’s first and middle name, and the sequence you’re trying to match on is that person’s first, middle, and last name. The partial_ratio() function will return a 100% match since the person’s first and middle name are the same.
# Token Sort Ratio
#  FuzzyWuzzy also has token functions that tokenize the strings, change capitals to lowercase, and remove punctuation. The token_sort_ratio() function sorts the strings alphabetically and then joins them together. Then, the fuzz.ratio() is calculated. This can come in handy when the strings you are comparing are the same in spelling but are not in the same order.
Str_A = 'Gunner William Kline'
Str_B = 'Kline, Gunner William'
ratio = fuzz.token_sort_ratio(Str_A, Str_B)
print('Similarity score: {}'.format(ratio))
# token_set_ratio()
# The token_set_ratio() function is similar to the token_sort_ratio() function above, except it takes out the common tokens before calculating the fuzz.ratio() between the new strings. This function is the most helpful when applied to a set of strings with a significant difference in lengths.
Str_A = 'The 3000 meter steeplechase winner, Soufiane El Bakkali'
Str_B = 'Soufiane El Bakkali'
ratio = fuzz.token_set_ratio(Str_A, Str_B)
print('Similarity score: {}'.format(ratio))
