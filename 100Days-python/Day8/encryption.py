alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# Step1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.


# Step2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet by the shift amount and print the encrypted text.

def encrypt(original_text, shift_amount):
    cipher_text = "" # j




# Step4: What happens if you try to shift z forwards by 9? can you fix the code?
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount # 7 -> 9

        shifted_position %= len(alphabet) #0-25
        cipher_text += alphabet[shifted_position] # j

    print(f"Here is the encoded result: {cipher_text}")

# Step3: call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a message.

encrypt(original_text=text, shift_amount=shift)