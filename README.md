# README_AaryaaMoharir_Acm220004

# Driver.py 

This is the main program that handles user interaction. It launches Logger.py and EncryptionProgram.py as separate processes using pipes for communication.
It provides a menu-based interface for the user to set passwords, encrypt/decrypt messages, and view the history. It also logs all user commands and 
responses from the encryption program. It also maintains a session-based history of all encrypted/decrypted messages.
It ensures only alphabetic characters are used for encryption, decryption, and password commands and sends QUIT commands to terminate both the Logger
and Encryption programs upon exit.

# EncryptionProgram.py 

The encryption program is designed to process commands provided via standard input. It maintains a passkey used for encryption and decryption. 
The program supports four commands: PASS, which sets the passkey; ENCRYPT, which applies the Vigenère cipher to the provided text using the current passkey;
DECRYPT, which reverses the encryption; and QUIT, which exits the program. If an encryption or decryption command is given before a passkey is set,
the program will return an error. The encryption program outputs results in a structured format where successful operations return RESULT <output>, and errors
return ERROR <message>.

# Logger.py 

The logger program will accept a single command-line argument specifying the log file name. It will then continuously accept log messages from standard input, 
formatting them with a timestamp and action type before writing them to the log file. The format for log entries is: YYYY-MM-DD HH:MM [ACTION] MESSAGE. 
The logger will continue running until it receives the command "QUIT", after which it will terminate.

# Devlog.md 
The devlog is structured in a diary format that contains my thoughts before starting a programming session and after finishing it. It includes what I did during 
that session, how I felt about it, and what I plan to do in the future. 

# How to run the program 

The program can be run through the terminal using _python3 ./driver.py <name_of_logfile>_ 
It needs to be run using python3 

# What does the output mean 

These are what the actions in the logger mean.

START_LOGGER – Initiates the logging mechanism.
START_DRIVER – Starts the main driver program.
START_ENCRYPTION – Starts the encryption process.

USER_INPUT – Represents an input command from the user.
PASSWORD – User inputs a password-related command.
RESULT_PASSWORD – Confirms the password has been successfully set.

ENCRYPT_MESSAGE – Shows the message that is being encrypted.
ENCRYPT_RESULT – Displays the result of a encryption operation.
DECRYPT_MESSAGE – Shows the encrypted message that is being decrypted.
DECRYPT_RESULT – Displays the result of a decryption operation.

SHOW_HISTORY – Displays the command history.
QUIT – Terminates the session or program.

END_DRIVER – Indicates that the main driver program has exited.
END_ENCRYPTION – Signals that the encryption process has ended.
STOP_LOGGER – Stops the logging mechanism.
ERROR - An error occured 

# Error handling

If there is an error in the program (such as incorrect input or if the encryption process suddenly dies), 
it will be outputted to the console and to the log. However, the program will continue to run, the user will 
just be redirected to the main input screen if they enter an invalid choice. 