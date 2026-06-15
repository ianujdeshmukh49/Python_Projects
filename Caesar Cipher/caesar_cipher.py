# Caesar Cipher Program
# array of alphabets
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Encryption Function
def encrypt_message(message, shift):
    new_message = ""
    for letter in message.lower():
        if letter in alphabets:
            new_index = (alphabets.index(letter) + shift) % len(alphabets)
            new_message += alphabets[new_index]
        else:
            new_message += letter
    
    print("Encrypted:", new_message)

# Decryption Function
def decrypt_message(message, shift):
    new_message = ""
    for letter in message.lower():
        if letter in alphabets:
            new_index = (alphabets.index(letter) - shift) % len(alphabets)
            new_message += alphabets[new_index]
        else:
            new_message += letter
    
    print("Decrypted:", new_message)

# Main program
print("=== Caesar Cipher ===")
print("Type 'x' to exit\n")

while True:
    user_input = input('E/D : ')
    if user_input.lower() == 'x':
        print("Goodbye!")
        break
    
    message = input("Enter the message : ")
    shift = int(input("Shift: "))

    if user_input.lower() in ('e', 'd'):
        if user_input.lower() == 'e':
            encrypt_message(message, shift)
        else:
            decrypt_message(message, shift)
    else: 
        print("Invalid Entry! Use 'E' for Encrypt or 'D' for Decrypt\n")
