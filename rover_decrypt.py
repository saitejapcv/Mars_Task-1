

def decrypt(code):
	words = code.strip().split(" ")
	decrypted = []
	
	for word in words:
		decrypted_word = ""
		for i in range(len(word)):
			decrypted_word += chr(ord(word[i])-(i+1))
		decrypted.append(decrypted_word)
	return " ".join(decrypted)

encrypted = input("Encrypted Message: ")
print("Decrypted Message:" , decrypt(encrypted))
