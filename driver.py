import subprocess
from subprocess import Popen, PIPE
import os

def print_menu():
    print("\nMenu:")
    print("1. Password")
    print("2. Encrypt")
    print("3. Decrypt")
    print("4. History")
    print("5. Quit")

#main program takes in a log_file
def main(log_file):
    logger = Popen(
        ['python3', 'logger.py', log_file],
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE,
        encoding='utf8'
    )

    # Start the encryption process
    encryption = Popen(
        ['python3', 'encryptionProgram.py'],
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE,

        encoding='utf8'
    )

    logger.stdin.write("Driver program started")
    logger.stdin.flush()

    history = []
    password_history = []

    while True:
        print_menu()
        command = input("Enter command: ").strip().lower()
        if command == 'quit':
            logger.stdin.write("Driver program exit")
            logger.stdin.flush()
            logger.stdin.write("QUIT")  # quits the logger
            encryption.stdin.write("QUIT")  # quits the encryption program
            encryption.stdin.flush()
            logger.stdin.flush()
            break

        elif command == 'password':
            print("Choose an option:")
            print("1. Use a new password")
            print("2. Use a password from history")
            choice = input("Enter choice (1 or 2): ").strip()

            #they want to set a new passkey
            if choice == '1':
                password = input("Enter password: ").strip()
                print( "this is what you are trying to set your password to" + password)
                #set the passkey
                encryption.stdin.write(f"PASS {password}\n")
                if encryption.poll() is None:
                    encryption.stdin.flush()
                else:
                    print("Encryption process died unexpectedly.")
                password_history.append(password)
                encrypted_message = encryption.stdout.readline().rstrip()
                logger.stdin.write(encrypted_message)
                logger.stdin.flush()
                print("Passkey set successfully.")

            elif choice == '2':
                print("Password history:")
                for idx, password in enumerate(password_history):
                    print(f"{idx + 1}. {password}")
                selected = int(input("Select password from history: ").strip())
                selected_password = password_history[selected - 1]
                encryption.stdin.write(f"PASS {selected_password}\n")
                encryption.stdin.flush()
                encrypted_message = encryption.stdout.readline().rstrip()
                logger.stdin.write(encrypted_message)
                logger.stdin.flush()
                print("Passkey set from history.")
            else:
                print("Invalid choice.")
        elif command == 'encrypt':
            # Encrypt command
            print("Choose an option:")
            print("1. Use a new string")
            print("2. Use a string from history")
            choice = input("Enter choice (1 or 2): ").strip()

            if choice == '1':
                message = input("Enter string to encrypt: ").strip()
                print(message)
                encryption.stdin.write(f"ENCRYPT {message}\n" )
                encryption.stdin.flush()
                history.append(message)
                encrypted_message = encryption.stdout.readline().rstrip()
                logger.stdin.write(encrypted_message)
                logger.stdin.flush()
                string = encrypted_message.split("RESULT ", 1)[-1]
                history.append(string)
                print(f"Encrypted message: {string}")
            elif choice == '2':
                print("History:")
                for idx, item in enumerate(history):
                    print(f"{idx + 1}. {item}")
                selected = int(input("Select string from history: ").strip())
                selected_message = history[selected - 1]
                encryption.stdin.write(f"ENCRYPT {selected_message}\n" )
                encryption.stdin.flush()
                encrypted_message = encryption.stdout.readline().strip()
                logger.stdin.write(encrypted_message)
                logger.stdin.flush()
                string = encrypted_message.split("RESULT ", 1)[-1]
                history.append(string)
                print(f"Encrypted message: {string}")
            else:
                print("Invalid choice.")
        elif command == 'decrypt':
            # Decrypt command
            print("Choose an option:")
            print("1. Use a new string")
            print("2. Use a string from history")
            choice = input("Enter choice (1 or 2): ").strip()

            if choice == '1':
                message = input("Enter string to decrypt: ").strip()
                encryption.stdin.write(f"DECRYPT {message}\n" )
                encryption.stdin.flush()
                history.append(f"DECRYPT: {message}")
                decrypted_message = encryption.stdout.readline().strip()
                logger.stdin.write(decrypted_message)
                logger.stdin.flush()
                string = decrypted_message.split("RESULT ", 1)[-1]
                history.append(string)
                print(f"Decrypted message: {string}")
            elif choice == '2':
                print("History:")
                for idx, item in enumerate(history):
                    print(f"{idx + 1}. {item}")
                selected = int(input("Select string from history: ").strip())
                selected_message = history[selected - 1]
                encryption.stdin.write(f"DECRYPT {selected_message}\n" )
                encryption.stdin.flush()
                decrypted_message = encryption.stdout.readline().strip()
                logger.stdin.write(decrypted_message)
                logger.stdin.flush()
                string = decrypted_message.split("RESULT ", 1)[-1]
                history.append(string)
                print(f"Decrypted message: {decrypted_message}")
            else:
                print("Invalid choice.")
        elif command == 'history':
            # Show history
            print("History:")
            for item in history:
                print(item)
        else:
            print("Invalid command.")

if __name__ == '__main__':
            log_file = input("Enter the log file name: ").strip()
            main(log_file)