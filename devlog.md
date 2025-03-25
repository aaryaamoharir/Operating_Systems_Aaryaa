# Devlog

This is a developer log.

---

# 2025-03-09 18:46  
Created an initial logger file. Today I hope to get a basic setup of the program down and I've decided to use Python for this project.

---

# 2025-03-09 19:14  
Ended the session for today. I was going to start working on the driver program first, but it might be easier if I make sure the encryption is working fine, so I'll get started on that.
After a little bit of research, I can now understand what the Vigenère cipher does. It's essentially a more complicated Caesar cipher where the key (a string of letters) tells you how 
many positions to shift each letter of the message by. I was also able to get some good progress on the logger file and set it up so that I was able to enter multiple strings in my logger 
My next session I want to focus on the encryption program now that I have a better understanding of the Vigenere cipher. 

---

# 2025-03-10 18:24  
Finished the session for today. I completed the decryption part of the program.It was pretty straightforward since I could just subtract the 
values instead of adding. I also worked on the encryption program and the was also fairly straightforward. I realized one of the errors in my 
program calculates the value of a as 0 so it doesn't add enough letters to the final value. 

---

# 2025-03-18 13:38  
I need to start working on the driver program that will connect my logger and encryption program. I know I need to use pipes in order to connect the output of the two processes 
(logger and encryption program). I'm not entirely sure how to only log changes for only a specific run, so I'll need to look into that.  

---

# 2025-03-18 13:51  
I'm currently thinking of using an array to store the history. This could also store previous passwords, and since it's an array, I can delete the history once the program is over.  

---

# 2025-03-18 14:01  
Finished implementing the initial driver, but now I get to run it and see where all of my errors stem from!  

---

# 2025-03-18 14:24  
Once I submit a command to encryption, it closes the pipe, so it's not able to accept more commands.  

---

# 2025-03-18 14:41  
Finished the session. The reason it was closing the pipe was because of the way my encryption program was set up. I changed it so that it continues to run until it receives the QUIT message.  
I was able to finish the basic part of driver.pu but I need to better format the log file, add in error checking, and ensure that the user is only inputting allowed characters. I also need to add a way 
to exit once a person decides to use a string from history. This is what my logging looks like right now: 
Program started. ERROR: No passkey set. RESULT: Passkey set. RESULT: AARYAA. RESULT: AARYAA. Driver program exit. QUIT.  


---

# 2025-03-23 14:31  
Today I want to work on fixing my logger formatting. The issue with why the logger was not writing out individual commands per 
line was because I wasn't ending each logger message in a newline. I need to work on allowing a user to go back if they click on 
using commands from history and then decide to enter a newline instead. 

---
# 2025-03-23 19:22  
Ended the session today. I realized I needed a separate devlog file and a logger.py file so I had to go back 
and fix that by extracting all the logger details in the logger file. I also realized that I don't necessarily 
like how the logger is formatted currently, so I changed that during this session as well. I fixed up some of 
the statements and cleaned up my code a little bit. I also added logic to return to a place to enter a new string 
if they already entered history. 

---
# 2025-03-24 14:31  
Today I need to test out this program on the cs1 server. I also realized that I need to fix my devlog.md 
to not include the logger statements so I went ahead and fixed my devlog formatting. 

---
# 2025-03-24 19:22  
Ended the session today. I tested it out on the CS1 server and it seems like it is working as expected! I need to make a 
readme file which I'll work on later today. There was also a logic issue with my for statements so I fixed that as well!

---
# 2025-03-24 21:53
I'm adding finishing touches before I submit. There are some error output issues that I'm currently working on fixing. 
I hope this doesn't take too long and after that I should be ready to submit. 

# 2025-03-24 22:06
Submitting now! This project was definitely interesting and gave me a good foundation for how to use the python 
subprocess module. However, I apologize to the ta's in advance because the code is quite messy since I was 
constantly realizing that I forgot to account for certain edge cases or requirements. 