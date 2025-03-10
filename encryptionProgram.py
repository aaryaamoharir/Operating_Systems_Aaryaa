#command line arguments; first word is command and rest as the argument and return with response type and then output
import sys
passkey = None

def cipher(message, key, encrypt):
    result = ""
    key_length = len(key)
    i =0;
    #go through every line in cipher
    if( encrypt == True):
        for c in message:
            print(ord(c) - ord('A'))
            print((ord(key[i % key_length]) - ord('A')))
            c = (ord(c)- ord('A'))+ (ord(key[i % key_length]) - ord('A')) + 1
            print(c)
            c = (c % 26) + ord('A')
            print(chr(c))
            result += chr(c)
            i = i + 1




for line in sys.stdin:
    #gets the command line argument
    parts = line.strip().split(" ", 1)
    command = parts[0]
    argument = parts[1] if len(parts) > 1 else ""
    print(command)
    if command == "PASS":
        passkey = argument
        print("RESULT Passkey set")
    elif command == "ENCRYPT":
        if passkey is None:
            print("ERROR No passkey set")
        else:
            print("RESULT", cipher(argument, passkey, encrypt=True))
    elif command == "DECRYPT":
        if passkey is None:
            print("ERROR No passkey set")
        #else:
        #print("RESULT", vigenere_cipher(argument, passkey, encrypt=False))
    elif command == "QUIT":
        break
    else:
        print("ERROR Unknown command")
