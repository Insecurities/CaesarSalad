#Caesar Cipher solving tool by EnigmaMe

#Catches user input for the message to decipher - .upper is used to convert all text to uppercase

ciphertext = raw_input("Enter your ciphertext: ").upper()

#Defines the alphabet to use, this uses the standard A-Z alphabet- Can be changed
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#brute forces our text, trying all 26 combinations 
for shift in range(len(ALPHABET)):
	plaintext =''
	for symbol in ciphertext:
		if symbol in ALPHABET:
			position = ALPHABET.index(symbol)
			position = position - shift

			if position < 0:
				position = position + len(ALPHABET)
			plaintext = plaintext + ALPHABET[position]
		else:
			plaintext = plaintext + symbol
	#prints ALL outputs of combinations through 26
	print('Shift #{0}: {1}'.format(shift,plaintext))


