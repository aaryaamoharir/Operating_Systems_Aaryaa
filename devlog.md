# Devlog

This is a developer log.

---
### 2025-03-09 18:46 - [START]

Created an initial logger file. Today I hope to get a basic setup of the program down and I've decided to use python for this project

### 2025-03-09 18:47 - [Trial]

trying out if it'll allow me to write a second message to the same file

---
### 2025-03-09 19:14 - [DRIVER/ENCRYPTION]

I was going to start working on the driver program first but it might be easier if I make sure the encryption is working fine so I'll get started on that. After a little bit of research I can now understand what the Vigenère cipher does. It's essentially a more complicated caesar cipher where the key (a string of letters) tells you how many positions to shift each letter of the message by

---
### 2025-03-10 13:54 - [UPDATE]

Currently working on the encryption program. I understand how it works and plan to code the program. I'm currently thinking of implementing it with a loop that iteratres through the number of digits each digit in the message needs to be increased by 

---
### 2025-03-10 13:54 - [QUIT]



---
### 2025-03-10 14:34 - [ERRORS]

realized one of the errors is because my program calculate the value of A as 0 so it doesn't add enough letters for the final value

---
### 2025-03-10 18:06 - [DECRYPT]

starting work on the decrytion part of the algorithm. It should be fairly straight forward as I could just subtract the values instead of adding

---
### 2025-03-10 18:24 - [DECRYPTCOMPLETE]

completed the decryption part of the program

---
### 2025-03-18 13:38 - [DRIVER]

I need to start working on the driver program that will connect my logger and encryption program. I know I need to use pipes in order to connect the output of the two processes (logger and encryption program). I'm not entirely sure how to only log changes for only a specific run so I'll need to look into that. 

---
### 2025-03-18 13:38 - [EXIT]



---
### 2025-03-18 13:38 - []



---
### 2025-03-18 13:51 - [HISTORY]

I'm currently thinking of using an array to store the history. This could also store previous passwords and since it's an array, I can delete the history once the program is over

---
### 2025-03-18 14:01 - [PROGRESS]

finished implementing the inital driver but now I get to run it and see where all of my errors stem from!

---
### 2025-03-18 14:22 - [COMMAND:]

Set new password

---
### 2025-03-18 14:24 - [ERROR]

once I submit a command to encryption, it closes the pipe so it's not able to accept more commands

---
### 2025-03-18 14:24 - [QUIT]



---
### 2025-03-18 14:24 - []



---
### 2025-03-18 14:41 - [DRIVERISSUE]

the reason it was closing the pipe was because of the way my encrpytion program was set up. I changed it so that it continues to run until it recieves the QUIT message 

---
#
### 2025-03-18 17:26 - [PROGRESS]

the basic part of driver.py is completed but I need to better format the log file, add in error checking that ensures the user is only inputting allowed characters, add in a way to exit to enter a new string not in history 

---
### 2025-03-18 17:55 - [Driver]

program startedERROR No passkey setRESULT Passkey setRESULT AARYAARESULT AARYAADriver program exitQUIT

---
### 2025-03-21 14:31 - [PROGRESS]

The issue with why the logger was not writing out individual commands per line was because I wasn't ending each logger message in a newline. I need to work on allowing a user to go back if they click on using commands from history and then decide to enter in a newline instead

---
### 2025-03-21 15:28 - [CHANGES]

added logic to return to a place to enter a new string if they already entered history 

---
### 2025-03-23 15:15 - [PROGRESS]

I need to fix some of the statements and clean up my code a bit

---
### 2025-03-23 16:12 - [I]

realized that I don't necessarily like how the logger is formatted currently so I'll be changing that

---

### 2025-03-23 19:18 - [START_LOGGER] Logger started
### 2025-03-23 19:22 - [CHANGES] I realized I needed a seperate devlog file and a logger.py file 
### 2025-03-23 19:22 - [STOP_LOGGER] Logger stopped
