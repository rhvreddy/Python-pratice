alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    cipher_text = "" # j
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount # 7 -> 9

        shifted_position %= len(alphabet) #0-25
        cipher_text += alphabet[shifted_position] # j

    print(f"Here is the encoded result: {cipher_text}")


#Step1: create a function called decrypt() that takes original_text and shift_amount as 2 inputs.
#Step2: inside the decrypt() function, shift each lettter of the original_text forwards in the alphabet backwards by the shift_amount and print the decrypted text.

def decrypt(original_text, shift_amount):
    output_text = ""  # j
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount  # 7 -> 9

        shifted_position %= len(alphabet)  # 0-25
        output_text += alphabet[shifted_position]  # j

    print(f"Here is the encoded result: {output_text}")


#Step3: combine the encrypt() and decrypt() functions into a single function called caesar()
#use the value of the user chosen direction varibale to determine which functionallity to use.
# call the caasar function insted of encrypt/decrypt and pass in all the three variables. direction/text/shift

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""  # j
    for letter in original_text:

        if encode_or_decode == "decode":
            shift_amount *= -1


        shifted_position = alphabet.index(letter) + shift_amount  # 7 -> 9

        shifted_position %= len(alphabet)  # 0-25
        output_text += alphabet[shifted_position]  # j

    print(f"Here is the {encode_or_decode}d result: {output_text}")


caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)


decrypt(original_text=text, shift_amount=shift)