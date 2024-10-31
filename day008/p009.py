alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    new_text = []

    for letter in original_text:
        if letter in alphabet:
            index = [i for i, x in enumerate(alphabet) if x == letter]
            new_index = int(''.join(map(str, index)))

            new_text.append(alphabet[new_index + shift_amount])
        else:
            new_text.append(letter)

    new_text_str = ''.join(map(str, new_text))
    print(new_text_str)

if direction == "encode":
    encrypt(text, shift)
