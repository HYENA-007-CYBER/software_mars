# MaRS Recruitment Task #1 
**Platform:** Ubuntu Linux(Dual Booted)<br>
**Languages Used:** Bash, Python  

---
## **Overview**

This repository contains my solutions for the MaRS Recruitment task #1.<br>I have done coding for all questions on my own and i used chatgpt for a better understanding  on each question.<br>I have added neccessary comments in my code script.

---

### Project Completion Summary

- Completed **all Light Dose** problems (Bash scripting and terminal-based tasks)
- Completed **all Medium Dose** problems (Python-based logic, filtering, decoding)
- Completed **Hard Dose**:
  -  Problem 1: Obstacle Map & Pathfinding
  -  Problem 3: Behavior Tree Design
  -  Problem 2: [Not attempted]
---



---

## **Learnings & Approach of all problems**

###  **Light Dose**

####  Question 1 & Question 2: 
- I am not very much known to terminal commands in Linux.
- I just know some basic commands.

  **My Approach:**
- Gone through some you-tube vedios to get a idea about Linux Commands related to navigation, file handling, and permissions.
- Googled for unknown commands.
- I broke out the problem into individual checks and tested each block.
- Used `echo` and `if-else` blocks to validate system behavior step by step.
  
  **Script:**
- [light_1](./light_1st.sh)
- [light_2](./light_2nd.sh)
  
 **Screenshot of basic terminal commands done on terminal:**
- [Screenshot_1](./btc_ss_1.jpg)
- [Screenshot_2](./btc_ss_2.jpg)
  

---

###  **Medium Dose**

####  Question 1: Marker Navigation
- I just added 55 units to z co_ordinate to get new frame of reference
- And wrote a function to calculate distance from origin
- Got input co_ordinates from user


 **Script:**
- [medium-1](./medium_1st.py)

  ---


####  Question 2: Morse Decoder
- To get information about morse code for alphabets and numbers i used chatgpt.
- Built a Morse-to-text dictionary.
- Traversed through input and got corresponding decoded character from dictionary.
- It can give u decoded msg for big paragraphs witten in morse also.

 **Script:**
- [medium-2](./medium_2nd.py)

  ---


####  Question 3: Encrypted Message Decoding
- THE Logic was the characters shifted back according to its postion in the word
- Devoloped a code for it.
  
   **Script:**
- [medium-3](./medium_3rd.py)

---

####  Question 4: Data Filtering (Muchiko, Sanchiko, Hybrid)
- Implemented and compared three filtering strategies on noisy sensor data.
- Used standard deviation to compare between the filters.
- Two hybrid filters have been created.(refer to script below)

  **Script:**
- [medium-4](./medium_4th.py)

---

####  Question 5: Euler to Martian 4D Orientation
- I used chatgpt to understand quaternion math and conversion logic.
- Understood the term "Gimbal Lock"
- Developed a code for it
- Verified results using sample angle inputs and quaternion libraries.

**Script:**
- [medium-5](./medium_5th.py)

---

###  **Hard Dose**

####  Problem 1: Obstacle Map & Shortest Path
- I built a arena grid of 11*11 USING NUMPY
- READ THE [obstacle file](./sample.txt) and placed zeros with respect to center
- Implemented BFS to find the shortest navigable path.
- I have already done breadth first search algothirm in my BS IN DATA SCIENCE ONLINE DEGREE IN IIT MADRAS
- Refer code script for dettailled comments

  **Script:**
- [hard-1](./hard_1st.py)

---

####  Problem 3: Behavior Tree Design
- Designed a behavior tree to model rover decisions in a A4 sheet.
- Took reference from You-Tube.
- Used fallback and sequence nodes for clean logical flow.
- Understood the terms and wrote answer in paper.

  **Script:**
- [hard-3](./hard_3rd.pdf)


---
## **Pushing Files Into Github**

- All problems were written in text edittor in LINUX
- 3RD Question of hard dose is uploaded as pdf from Windows
- The files are pushed into github using terminal
- I created tokens to push my files
--- 

### **THE SCREENSHOT OF COMMANDS DONE IN TERMINAL**
-[ScreenShot - 1](./screenshot1.jpg)<br>
-[ScreenShot - 2](./screenshot2.jpg)<br>
-[ScreenShot - 3](./screenshot3.jpg)<br>
- After this i done this command in terminal: [ git commit -m "medium" ] and pushed the files to github repo
- I forgot to take ScreenShot of it and closed the terminal.

  ---

## **Participation in Maze Rover**

- I went through the github repo and installed ros 
- I Played the game and completed the maze for Round 1
- For Round 2 I was going through the coding part
- Since my laptop is comparitively old one , installation of ros took a lot of time and i didnt get much time to complete the coding round

--- 


  
  







