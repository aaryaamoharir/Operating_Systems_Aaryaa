#command line arguments; first word is command and rest as the argument and return with response type and then output
import sys
passkey = None

def cipher(message, key, encrypt):
    result = ""
    key = key.upper()
    message = message.upper()
    key_length = len(key)
    i =0;
    #go through every line in cipher
    if( encrypt == True):
        for c in message:
            c = (ord(c)- ord('A'))+ (ord(key[i % key_length]) - ord('A'))
            c = (c % 26) + ord('A')
            result += chr(c)
            i = i + 1
        return result
    if (encrypt == False):
        for c in message:
            c = (ord(c)- ord('A') )- ((ord(key[i % key_length]) - ord('A')))
            c = (c % 26) + ord('A')
            result += chr(c)
            i = i + 1
        return result




for line in sys.stdin:
    #gets the command line argument
    parts = line.strip().split(" ", 1)
    command = parts[0]
    argument = parts[1] if len(parts) > 1 else ""
    if command == "PASS":
        passkey = argument
        print("RESULT Passkey set" , flush=True)
    elif command == "ENCRYPT":
        if passkey is None:
            print("ERROR No passkey set", flush=True)
        else:
            print("RESULT", cipher(argument, passkey, encrypt=True), flush=True)
    elif command == "DECRYPT":
        if passkey is None:
            print("ERROR No passkey set")
        #else:
        print("RESULT", cipher(argument, passkey, encrypt=False), flush=True)
    elif command == "QUIT":
        break
    else:
        print("ERROR Unknown command")
