original = input("Enter a Sentence: ").strip().lower()
words = original.split()
new_words = []
for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vow_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vow_pos = vow_pos + 1
            else:
                break
        cons = word[:vow_pos]
        rest = word[vow_pos:]
        new_word = rest + cons +"ay"
        new_words.append(new_word)
output = " ".join(new_words).capitalize()
print(output)




