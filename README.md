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

It you get an error that says invalid input it could be because history holds no information and therefore, a string from history 
cannot be chosen and it will redirect you to the main options once again. USER_INPUT in the log file includes what the user inputted, 

# Error handling