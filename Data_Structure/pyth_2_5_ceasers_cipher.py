### Ceasers Cipher ###


shift = int(3)
text = "zebra"

#letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z"]
letters ="abcdefghijklmnopqrstuvwxyz"


def enigma(message, shift):
    secret_message = " "
    for letter in message:
        letter = letter.lower()
        if not letter == " ":
            i = letters.find(letter)
            if i == -1: 
                secret_message += letter
            else:
                j = i + shift
                if j >= 26:
                    j -= 26    
                secret_message += letters[j] 
    return secret_message             

secret_message = enigma(text, shift)

print(f"Secret message: {secret_message}")


#### Anoj Solution. #####

def ceasar_cipher():
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    message = input("Enter secret message: ").lower()
    shift = int(input("Enter shift number: "))

    encrypted_message = ""

    for char in message:
        if char in alphabet:
            # Find the original index
            current_index = alphabet.index(char)

            # Calculate the new index with wrap-around
            new_index = (current_index + shift) % 26

            # Get the new value using the new index
            new_char = alphabet[new_index]

            encrypted_message += new_char

        else:
            encrypted_message += char

    print(encrypted_message)


ceasar_cipher()