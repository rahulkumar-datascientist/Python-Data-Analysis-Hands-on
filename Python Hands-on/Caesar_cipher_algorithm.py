"""
   written by : Rahul Kumar
   Date       : 14/11/2019
   
   Caesar cipher
    Implement a Caesar cipher, both encoding and decoding. The key is an integer
    from 1 to 25. This cipher rotates the letters of the alphabet (A to Z). The
    encoding replaces each letter with the 1st to 25th next letter in the alphabet
    (wrapping Z to A). So key 2 encrypts "HI" to "JK", but key 20 encrypts "HI" to
    "BC". This simple "monoalphabetic substitution cipher" provides almost no
    security, because an attacker who has the encoded message can either use
    frequency analysis to guess the key, or just try all 25 keys.
"""

VALID_STRING = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(text,key):
    # used to encrypt a given input text
    # 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    
    encrypt_string = 'abcdefghijklmnopqrstuvwxyz' * 2
    output = ''
    for char in text:
        if char in VALID_STRING:
            index = encrypt_string.index(str(char))
            output += encrypt_string[index+key]
        else:
            output += char
    return output

def decrypt(text,key):
    # used to decrypt a given encrypted text
    # 'zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba'
    
    decrypt_string = 'zyxwvutsrqponmlkjihgfedcba' * 2
    output = ''
    for char in text:
        if char in VALID_STRING:
            index = decrypt_string.index(str(char))
            output += decrypt_string[index+key]
        else:
            output += char
    return output

if __name__ == '__main__':
    
    print("1. Press 1 to Encrypt text \n2. Press 2 to Decrypt text \n3. Press 3 to do both \n")
    
    choice = input('Enter a choice: ')
        
    if choice == '1':
        input_txt = input('Enter the text to encrypt:')
        key       = int(input('Enter Key between 1 to 25 :'))
        print("The encrypted text is : ")
        print(encrypt(input_txt, key))
        
    elif choice == '2':
        input_txt = input('Enter the text to decrypt:')
        key       = int(input('Enter Key between 1 to 25 :'))
        print("The decrypted text is : ")
        print(decrypt(input_txt, key))

    elif choice == '3':
        input_txt = input('Enter the text:')
        key       = int(input('Enter Key between 1 to 25 :'))
        
        print("The encrypted text is : ")
        decrypt_txt = encrypt(input_txt, key)
        print(encrypt(input_txt, key))
        
        print("The decrypted text is : ")
        print(decrypt(decrypt_txt, key))
    else:
        print('Invalid choice')
