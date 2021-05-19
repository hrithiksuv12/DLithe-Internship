#Defining a function to encrypt the message
def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isspace():
            result += " "
        elif char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

#Defining a function to decrypt the message
def decrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isspace():
            result += " "
        elif char.isupper():
            result += chr((ord(char) - 65) % 26 + (65 - s))
        else:
            result += chr((ord(char) - 97) % 26 + (97 - s))
    return result

#Obtaining user inputs
text = input("Enter the text: ")
s = int(input("Enter the value of shift: "))
op = str(input("Enter e/d to encrypt/decrypt: "))

#To encrypt or decrypt the message
if op == "e":
    print("Text    : ", text)
    print("Shift   : ", str(s))
    print("Encypher: ", encrypt(text, s))
elif op == "d":
    print("Text    : ", text)
    print("Shift   : ", str(s))
    print("Decypher: ", decrypt(text, s))
else:
    print("Enter a valid input")