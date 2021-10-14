## imports and framework
import string # get string module [test with string.printable]

char_set = string.printable[:-5] # get rid of control characters
substitution_chars = char_set[-3:] + char_set[:-3] # duplicate charset, shift by 3 letters [test with [substitution_chars]

encryption_dict = {} # create encryption dictionary (AKA map regular alphabet to cypher alphabet)
decryption_dict = {} #     |_ decryption _|               |_ cypher _|        |_ regular _|

for i, c in enumerate(char_set): # 0 refers to '0', 15 refers to 'f', etc.
    v = substitution_chars[i] 
    encryption_dict[c] = v
    decryption_dict[v] = c


## functions for encrypting/decrypting text: 
def encrypt(msg, encrypt_dict): # create list of characters, stitch into single string
    cipher = []
    for c in msg:
        v = encrypt_dict[c] 
        cipher += v
    return ''.join(cipher)

def decrypt(msg, decrypt_dict): # as above, so below
    plain = []
    for c in msg:
        v = decrypt_dict[c]
        plain += v
    return ''.join(plain)

# testing encryption + decryption
encrypt("giulia", encryption_dict)
decrypt("dfrif7", decryption_dict)





