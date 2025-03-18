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
