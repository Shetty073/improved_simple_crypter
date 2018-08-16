import string

def start():
	try:
		choice = int(
			input("Enter 1 for encrypting and 2 for decrypting: (1 or 2)\n>>> "))
		if choice < 1 or choice > 2:
			print("invalid input! value must be 1 or 2\nTry again...")
			start()
		else:
			print(cipher(choice))
	except Exception as e:
		print(f"Error occurred! Error code: {e}\nTry again...")
		start()

def cipher(choice):
	opt = {1:"encrypt", 2: "decrypt"}
	alph = string.ascii_letters + " "
	msg = input(f"Enter the message to {opt[choice]}:\n>>> ")
	strKey = int(input(f"Enter the key for {opt[choice]}ion:\n>>> "))
	key = int(strKey)
	newMsg = ""
	for char in msg:
		if char in alph:
			pos = alph.find(char)
			if choice == 1:
				newPos = (pos + key) % 53
			elif choice == 2:
				newPos = (pos - key) % 53
			newChar = alph[newPos]
			newMsg += newChar
		else:
			newMsg += char
	return f"Encrypted message:\n>>> {newMsg}"

start()
