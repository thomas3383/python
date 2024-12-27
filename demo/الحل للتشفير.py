import string

def encrypted(message, shift):
    alphabet = string.ascii_lowercase
    encrypted_message = ""

    for letter in message:
        if letter.lower() in alphabet:
            original_position = alphabet.index(letter.lower())
            new_position = (original_position + shift) % 26

            encrypted_letter = alphabet[new_position]

            if letter.isupper():
                encrypted_letter = encrypted_letter.upper()

            encrypted_message += encrypted_letter
        else:
            encrypted_message += letter

    print(f"The encrypted message is:\n************\n{encrypted_message}\n************\n")

user_message = input("Enter a message: ")
shift_number = int(input("Enter a shift number: "))

encrypted(message = user_message, shift = shift_number)
