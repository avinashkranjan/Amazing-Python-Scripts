alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
			'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
			'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text1, shift1, direction1):
	end_text = ''
	if direction=='decode':
		shift1 *= -1

	for char in text1:
		if char in alphabet:
			position = alphabet.index(char)
			new_position = position + shift1
			end_text += alphabet[new_position]
		else:
			end_text += char
	print(f'The {direction1}d text is: {end_text}.')


should_continue = True
while should_continue:
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	shift = shift % 25

	caesar(text, shift, direction)
	choice=input("Type 'yes' to continue otherwise type 'no'.\n")
	if choice == 'no':
		should_continue=False 
