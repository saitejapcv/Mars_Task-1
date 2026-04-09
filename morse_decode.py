# Morse Code Dictionary
MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z',

    '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9'
}

def morse_decode(morse_code):
	words = morse_code.strip().split("   ") # according to morse code 3 spaces is 1 space between words.
	decoded_message = []
	
	for word in words:
		letters = word.split(" ") # 1 space = new letter
		decoded_word = ""
		
		for letter in letters: 
			if letter in MORSE_CODE_DICT:
				decoded_word += MORSE_CODE_DICT[letter]
		decoded_message.append(decoded_word)
		
	return " ".join(decoded_message)

morse_input = input("Morse Code: ")
print("Decoded Message:", morse_decode(morse_input))
		
	
