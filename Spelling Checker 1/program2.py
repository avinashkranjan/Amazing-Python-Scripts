from spellchecker import SpellChecker

spell = SpellChecker()

# find those words that may be misspelled
misspelled = spell.unknown(["cmputr", "watr", "study", "wrte"])

for word in misspelled:
	# Get the one `most likely` answer
	print(spell.correction(word))

	# Get a list of `likely` options
	print(spell.candidates(word))

/*
Output: 
computer
{'caput', 'caputs', 'compute', 'computor', 'impute', 'computer'}
water
{'water', 'watt', 'warr', 'wart', 'war', 'wath', 'wat'}
write
{'wroe', 'arte', 'wre', 'rte', 'wrote', 'write'} 
*/

