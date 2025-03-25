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

    logger.stdin.write("START_DRIVER Driver program started\n")
    logger.stdin.flush()
    logger.stdin.write("START_ENCRYPTION Encryption program started\n")
    logger.stdin.flush()

    history = []
    #password_history = []

    while True:
        print_menu()
        command = input("Enter command: ").strip().upper()
        logger.stdin.write("USER_INPUT " + command + "\n")
        logger.stdin.flush()

        if command == 'QUIT':
            logger.stdin.write("END_DRIVER Driver program exit\n")
            logger.stdin.flush()
            logger.stdin.write("END_ENCRYPTION Encryption program exit\n")
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
                logger.stdin.write("USER_INPUT Use a password from history\n")
                logger.stdin.flush()
                for idx, password in enumerate(history):
                    print(f"{idx + 1}. {password}")
                if (len(history) <= 0):
                    selected = int(input(
                        "There are no values in history so type -1 to enter a new string instead: ").strip())
                else:
                    selected = int(input("Select password from history (please select numbers only) or type -1 to enter a new string instead: ").strip())
                if not is_valid_numbers(selected):
                    print("ERROR Invalid input! Input can only contain numbers.")
                    logger.stdin.write("ERROR " + " Invalid input! Input can only contain numbers" + "\n")
                    logger.stdin.flush()
                    continue
                logger.stdin.write("USER_INPUT " + str(selected) + "\n")
                if str(selected) == '-1':
                    choice = '1'
                if choice == '2':
                    if (not is_valid_numbers(selected)) or (selected > len(history)):
                        print( "ERROR " + " Invalid input! Input can only contain numbers and must be one of the options shown above" + "\n")
                        logger.stdin.write("ERROR" + " Invalid input! Input can only contain numbers and must be one of the options shown above" +   "\n")
                        logger.stdin.flush()
                    else:
                        selected_password = history[selected - 1]
                        encryption.stdin.write(f"PASS {selected_password}\n")
                        encryption.stdin.flush()
                        encrypted_message = encryption.stdout.readline().rstrip()
                        logger.stdin.write("RESULT_PASSWORD " + encrypted_message + "\n")
                        logger.stdin.flush()
                        print("Passkey set from history.")
            if choice == '1':
                password = input("Enter password (numbers only): ").strip().upper()
                logger.stdin.write("USER_INPUT Use a new password\n")
                logger.stdin.flush()

                if not is_valid_input(password):
                    print("ERROR Invalid input! Password can only contain letters (A-Z, a-z).")
                    logger.stdin.write("ERROR " + " Invalid input! Password can only contain letters (A-Z, a-z)" + "\n")
                    logger.stdin.flush()
                    continue
                #set the passkey
                encryption.stdin.write(f"PASS {password}\n")
                if encryption.poll() is None:
                    encryption.stdin.flush()
                else:
                    print("ERROR Encryption process died unexpectedly.")
                    logger.stdin.write("ERROR " + " Encryption process died unexpectedly." + "\n")
                    logger.stdin.flush()
                encrypted_message = encryption.stdout.readline().rstrip()
                logger.stdin.write("RESULT_PASSWORD " + encrypted_message + "\n")
                logger.stdin.flush()
                print("Passkey set successfully.")
            if (choice != '1' and choice != '2' and choice != '-1'):
                logger.stdin.write("ERROR " + " Invalid Choice" + "\n")
                logger.stdin.flush()
                print("ERROR Invalid choice.")
        elif command == 'ENCRYPT':
            # Encrypt command
            print("Choose an option:")
            print("1. Use a new string")
            print("2. Use a string from history")
            choice = input("Enter choice (1 or 2): ").strip()
            if not is_valid_numbers(choice):
                print("ERROR Invalid input! Input can only contain numbers.")
                logger.stdin.write("ERROR " + " Invalid input! Input can only contain numbers" + "\n")
                logger.stdin.flush()
                continue

            #User chose to enter a string from history
            if choice == '2':
                logger.stdin.write("USER_INPUT Use a string from history\n")
                logger.stdin.flush()
                for idx, item in enumerate(history):
                    print(f"{idx + 1}. {item}")
                if (len(history) <= 0):
                    selected = int(input(
                        "There are no values in history so type -1 to enter a new string instead: ").strip())
                else:
                    selected = int(input(
                        "Select password from history (please select numbers only) or type -1 to enter a new string instead: ").strip())

                if not is_valid_numbers(selected):
                    print("ERROR Invalid input! Input can only contain numbers.")
                    logger.stdin.write("ERROR " + " Invalid input! Input can only contain numbers" + "\n")
                    logger.stdin.flush()
                    continue
                logger.stdin.write("USER_INPUT " + str(selected) + "\n")

                if str(selected) == '-1':
                    choice = '1'
                if choice == '2':
                    if (not is_valid_numbers(selected)) or (selected > len(history)):
                        print( "ERROR" + " Invalid input! Input can only contain numbers and must be one of the options shown above" + "\n")
                        logger.stdin.write("ERROR" + " Invalid input! Input can only contain numbers and must be one of the options shown above" +   "\n")
                        logger.stdin.flush()
                        continue
                    else:
                        selected_message = history[selected - 1]
                        logger.stdin.write("ENCRYPT_MESSAGE " + selected_message + "\n")
                        logger.stdin.flush()
                        encryption.stdin.write(f"ENCRYPT {selected_message}\n" )
                        encryption.stdin.flush()
                        encrypted_message = encryption.stdout.readline().strip()
                        if encrypted_message.startswith("ERROR"):
                            print(encrypted_message)
                            logger.stdin.write(encrypted_message +  "\n")
                            logger.stdin.flush()
                            continue
                        #get the result of the encrypted string
                        string = encrypted_message.split("RESULT ", 1)[-1]
                        history.append(string)
                        print(f"RESULT Encrypted message: {string}")
                        logger.stdin.write("ENCRYPT_RESULT " + string + "\n")
                        logger.stdin.flush()
            if choice == '1':
                message = input("Enter string to encrypt: ").strip().upper()
                logger.stdin.write("USER_INPUT Use a new string to encrypt\n")
                logger.stdin.flush()

                if not is_valid_input(message):
                    print("ERROR Invalid input! Message can only contain letters (A-Z, a-z).")
                    logger.stdin.write("ERROR " + "Invalid input! Message can only contain letters (A-Z, a-z)." + "\n")
                    logger.stdin.flush()
                    continue
                encryption.stdin.write(f"ENCRYPT {message}\n" )
                encryption.stdin.flush()
                logger.stdin.write("ENCRYPT_MESSAGE " + message + "\n")
                logger.stdin.flush()
                history.append(message)
                encrypted_message = encryption.stdout.readline().rstrip()
                if encrypted_message.startswith("ERROR"):
                    print(encrypted_message)
                    logger.stdin.write(encrypted_message + "\n")
                    logger.stdin.flush()
                    continue
                string = encrypted_message.split("RESULT ", 1)[-1]
                history.append(string)
                logger.stdin.write("ENCRYPT_RESULT " + string + "\n")
                logger.stdin.flush()
                print("RESULT Encrypted message:" + string)
            if( choice != '1' and choice != '2' and choice != '-1'):
                print(choice)
                print("ERROR Invalid choice for encrypt.")
                logger.stdin.write("ERROR Invalid Choice" + "\n")
                logger.stdin.flush()
        elif command == 'DECRYPT':
            # Decrypt command
            print("Choose an option:")
            print("1. Use a new string")
            print("2. Use a string from history")
            choice = input("Enter choice (1 or 2): ").strip()
            if not is_valid_numbers(choice):
                print("ERROR Invalid input! Input can only contain numbers.")
                logger.stdin.write("ERROR " + " Invalid input! Input can only contain numbers" + "\n")
                logger.stdin.flush()
                continue

            if choice == '2':
                logger.stdin.write("USER_INPUT Use a string from history\n")
                logger.stdin.flush()
                print("History:")
                for idx, item in enumerate(history):
                    print(f"{idx + 1}. {item}")
                if (len(history) <= 0):
                    selected = int(input(
                        "There are no values in history so type -1 to enter a new string instead: ").strip())
                else:
                    selected = int(input(
                        "Select password from history (please select numbers only) or type -1 to enter a new string instead: ").strip())
                if not is_valid_numbers(selected):
                    print("ERROR Invalid input! Input can only contain numbers.")
                    logger.stdin.write("ERROR " + " Invalid input! Input can only contain numbers" + "\n")
                    logger.stdin.flush()
                    continue
            logger.stdin.write("USER_INPUT " + str(selected) + "\n")

            if str(selected) == '-1':
                    choice = '1'
            if choice == '2':
                if (not is_valid_numbers(selected)) or (selected > len(history)):
                    print("ERROR Invalid input! Input can only contain numbers and must be one of the options shown above")
                    logger.stdin.write("ERROR" + " Invalid input! Input can only contain numbers and must be one of the options shown above" + "\n")
                    logger.stdin.flush()
                    continue
                else:
                    selected_message = history[selected - 1]
                    encryption.stdin.write(f"DECRYPT {selected_message}\n" )
                    logger.stdin.write("DECRYPT_MESSAGE " + selected_message + "\n")
                    logger.stdin.flush()
                    encryption.stdin.flush()
                    decrypted_message = encryption.stdout.readline().strip()
                    if decrypted_message.startswith("ERROR"):
                        print(decrypted_message)
                        logger.stdin.write(decrypted_message + "\n")
                        logger.stdin.flush()
                        continue

                    string = decrypted_message.split("RESULT ", 1)[-1]
                    logger.stdin.write("DECRYPT_RESULT " + string + "\n")
                    logger.stdin.flush()
                    history.append(string)
                    print(f"RESULT Decrypted message: {decrypted_message}")

            if choice == '1':
                message = input("Enter string to decrypt: ").strip()
                if not is_valid_input(message):
                    print("ERROR Invalid input! Message can only contain letters (A-Z, a-z).")
                    logger.stdin.write("ERROR " + "Invalid input! Message can only contain letters (A-Z, a-z)." + "\n")
                    logger.stdin.flush()
                    continue
                encryption.stdin.write(f"DECRYPT {message}\n" )
                encryption.stdin.flush()
                logger.stdin.write("DECRYPT_MESSAGE " + message + "\n")
                logger.stdin.flush()
                history.append(message)
                decrypted_message = encryption.stdout.readline().strip()
                if decrypted_message.startswith("ERROR"):
                    print(decrypted_message)
                    logger.stdin.write(decrypted_message + "\n")
                    logger.stdin.flush()
                    continue
                string = decrypted_message.split("RESULT ", 1)[-1]
                history.append(string)
                logger.stdin.write("DECRYPT_RESULT " + string + "\n")
                logger.stdin.flush()

                print(f"RESULT Decrypted message: {string}")
            if (choice != '1' and choice != '2' and choice != '-1'):
                print("ERROR Invalid choice.")
                logger.stdin.write("ERROR " + " Invalid choice" + "\n")
                logger.stdin.flush()
        elif command == 'HISTORY':
            # Show history
            logger.stdin.write("SHOW_HISTORY " + "\n")
            logger.stdin.flush()
            print("History:")
            for item in history:
                print(item)
        else:
            print("ERROR Invalid command.")
            logger.stdin.write("ERROR " + " Invalid choice" + "\n")
            logger.stdin.flush()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 driver.py <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]
    main(log_file)