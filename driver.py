import subprocess
from subprocess import Popen, PIPE
import os
import re
import sys

def print_menu():
    print("\nMenu:")
    print("1. Password")
    print("2. Encrypt")
    print("3. Decrypt")
    print("4. History")
    print("5. Quit")


def is_valid_input(text):
    return bool(re.fullmatch(r"[A-Za-z]+", text))

def is_valid_numbers(input_str):
    return str(input_str).lstrip("-").isdigit()

#main program takes in a log_file
def main(log_file):
    logger = Popen(
        ['python3', 'logger.py', log_file],
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE,
        encoding='utf8'
    )

    encryption = Popen(
        ['python3', 'encryptionProgram.py'],
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE,
        encoding='utf8'
    )

    logger.stdin.write("START Driver program started\n")
    logger.stdin.flush()

    history = []
    password_history = []

    while True:
        print_menu()
        command = input("Enter command: ").strip().upper()
        logger.stdin.write("Command: " + command + "\n")
        logger.stdin.flush()

        if command == 'QUIT':
            logger.stdin.write("END Driver program exit\n")
            logger.stdin.flush()
            logger.stdin.write("QUIT\n")  # quits the logger
            encryption.stdin.write("QUIT")  # quits the encryption program
            break

        elif command == 'PASSWORD':
            print("Choose an option:")
            print("1. Use a new password")
            print("2. Use a password from history")
            choice = input("Enter choice (1 or 2): ").strip()

            #they want to set a new passkey
            if choice == '2':
                print("Password history:")
                logger.stdin.write("Choice: Use a password from history\n")
                logger.stdin.flush()
                for idx, password in enumerate(password_history):
                    print(f"{idx + 1}. {password}")
                selected = int(input("Select password from history (please select letters only) or type -1 to enter a new string instead: ").strip())
                if not is_valid_numbers(selected):
                    print("Invalid input! Input can only contain numbers.")
                    continue
                if str(selected) == '-1':
                    choice = '1'
                if str(selected) == '2':
                    selected_password = password_history[selected - 1]
                    encryption.stdin.write(f"PASS {selected_password}\n")
                    encryption.stdin.flush()
                    encrypted_message = encryption.stdout.readline().rstrip()
                    logger.stdin.write(encrypted_message + "\n")
                    logger.stdin.flush()
                    print("Passkey set from history.")
            if choice == '1':
                password = input("Enter password (letters only): ").strip().upper()
                logger.stdin.write("Choice: Use a new password\n")
                logger.stdin.flush()

                if not is_valid_input(password):
                    print("Invalid input! Password can only contain letters (A-Z, a-z).")
                    continue
                #set the passkey
                encryption.stdin.write(f"PASS {password}\n")
                if encryption.poll() is None:
                    encryption.stdin.flush()
                else:
                    print("Encryption process died unexpectedly.")
                password_history.append(password)
                encrypted_message = encryption.stdout.readline().rstrip()
                logger.stdin.write(encrypted_message + "\n")
                logger.stdin.flush()
                print("Passkey set successfully.")
            else:
                print("Invalid choice.")
        elif command == 'ENCRYPT':
            # Encrypt command
            print("Choose an option:")
            print("1. Use a new string")
            print("2. Use a string from history")
            choice = input("Enter choice (1 or 2): ").strip()

            if choice == '2':
                logger.stdin.write("Choice: Use a string from history\n")
                logger.stdin.flush()
                for idx, item in enumerate(history):
                    print(f"{idx + 1}. {item}")
                selected = int(input("Select password from history (please select letters only) or type -1 to enter a new string instead: ").strip())
                if not is_valid_numbers(selected):
                    print("Invalid input! Input can only contain numbers.")
                if str(selected) == '-1':
                    choice = '1'
                if choice == '2':
                    selected_message = history[selected - 1]
                    encryption.stdin.write(f"ENCRYPT {selected_message}\n" )
                    encryption.stdin.flush()
                    encrypted_message = encryption.stdout.readline().strip()

                    logger.stdin.write(encrypted_message + "\n")
                    logger.stdin.flush()
                    if encrypted_message.startswith("ERROR"):
                        print(encrypted_message)
                        continue
                    string = encrypted_message.split("RESULT ", 1)[-1]
                    history.append(string)
                    string = encrypted_message.split("RESULT ", 1)[-1]
                    history.append(string)
                    print(f"Encrypted message: {string}")
            if choice == '1':
                message = input("Enter string to encrypt: ").strip().upper()
                logger.stdin.write("Choice: Use a new string\n")
                logger.stdin.flush()

                if not is_valid_input(message):
                    print("Invalid input! Message can only contain letters (A-Z, a-z).")
                    continue
                print(message)
                encryption.stdin.write(f"ENCRYPT {message}\n" )
                encryption.stdin.flush()
                history.append(message)
                encrypted_message = encryption.stdout.readline().rstrip()
                logger.stdin.write(encrypted_message + "\n")
                logger.stdin.flush()
                if encrypted_message.startswith("ERROR"):
                    print(encrypted_message)
                    continue
                string = encrypted_message.split("RESULT ", 1)[-1]
                history.append(string)
            else:
                print("Invalid choice.")
        elif command == 'DECRYPT':
            # Decrypt command
            print("Choose an option:")
            print("1. Use a new string")
            print("2. Use a string from history")
            choice = input("Enter choice (1 or 2): ").strip()

            if choice == '2':
                print("History:")
                for idx, item in enumerate(history):
                    print(f"{idx + 1}. {item}")
                selected = int(input("Select password from history (please select letters only) or type -1 to enter a new string instead: ").strip())
                if str(selected) == '-1':
                    choice = '1'
                if choice == '2':
                    selected_message = history[selected - 1]
                    encryption.stdin.write(f"DECRYPT {selected_message}\n" )
                    encryption.stdin.flush()
                    decrypted_message = encryption.stdout.readline().strip()
                    if not is_valid_numbers(decrypted_message):
                        print("Invalid input! Input can only contain numbers.")
                    logger.stdin.write(decrypted_message + "\n")
                    logger.stdin.flush()
                    if decrypted_message.startswith("ERROR"):
                        print(decrypted_message)
                        continue
                    string = decrypted_message.split("RESULT ", 1)[-1]
                    history.append(string)
                    print(f"Decrypted message: {decrypted_message}")

            if choice == '1':
                message = input("Enter string to decrypt: ").strip()
                if not is_valid_input(message):
                    print("Invalid input! Message can only contain letters (A-Z, a-z).")
                    continue
                encryption.stdin.write(f"DECRYPT {message}\n" )
                encryption.stdin.flush()
                history.append(message)
                decrypted_message = encryption.stdout.readline().strip()
                logger.stdin.write(decrypted_message + "\n")
                logger.stdin.flush()
                if decrypted_message.startswith("ERROR"):
                    print(decrypted_message)
                    continue
                string = decrypted_message.split("RESULT ", 1)[-1]
                history.append(string)
                print(f"Decrypted message: {string}")
            else:
                print("Invalid choice.")
        elif command == 'HISTORY':
            # Show history
            print("History:")
            for item in history:
                print(item)
        else:
            print("Invalid command.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 driver.py <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]
    main(log_file)