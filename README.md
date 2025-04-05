# MaRS Recruitment Task #1 
**Platform:** Ubuntu Linux(Dual Booted)<br>
**Languages Used:** Bash, Python  

---
## **1. Overview**

This repository contains my solutions for the MaRS Recruitment task #1.<br>I have done coding for all questions on my own and i used chatgpt for a better understanding  on each question.<br>I have added neccessary comments in my code script.

---

### Project Completion Summary

- Completed **all Light Dose** problems (Bash scripting and terminal-based tasks)
- Completed **all Medium Dose** problems (Python-based logic, filtering, decoding, and orientation)
- Completed **Hard Dose**:
  -  Problem 1: Obstacle Map & Pathfinding
  -  Problem 3: Behavior Tree Design
  -  Problem 2: [Not attempted]
---


## **7. Overall Learning Experience**

Working through the MaRS Recruitment Task was both intellectually stimulating and highly rewarding. Here's what I gained from this experience:

- **System-Level Thinking:** Through the Bash scripting and Linux-based tasks, I developed a deeper understanding of how real rover systems might operate, with emphasis on diagnostics, file handling, and command-line automation.

- **Algorithmic Problem Solving:** The Medium Dose challenges helped sharpen my skills in string processing, cipher breaking, spatial logic, and filtering algorithms — all essential in autonomous robotics and embedded systems.

- **Mathematical Modeling & Orientation:** Implementing 3D to 4D orientation conversions introduced me to quaternions and their role in spatial navigation, which is crucial for robotics and aerospace applications.

- **Data Noise Handling:** Comparing different filters (Muchiko, Sanchiko, Hybrid) gave me practical insight into how sensor data can be cleaned for real-time decision-making.

- **Pathfinding & Grid Analysis:** In the Hard Dose, I learned how to build and navigate grid-based maps using BFS. This solidified my understanding of graph traversal in constrained environments.

- **Behavior Tree Design:** Creating a decision-making structure for the rover taught me how complex logic can be broken down into maintainable, visual components — a powerful concept in robotics programming.

- **Version Control & Documentation:** Throughout the task, I followed Git best practices and wrote clear, structured documentation to reflect industry-level coding standards.

> 🚀 Overall, this challenge felt like a real-world mission planning exercise. It tested my logic, coding clarity, and ability to think like a robotic systems engineer — and I thoroughly enjoyed the journey.

---

## **6. Learnings & Approach of all problems**

###  **Light Dose**

#### 🔹 Question 1 & Question 2: 
- I am not very much known to terminal commands in Linux.
- I just know some basic commands.

  **My Approach:**
- Gone through some you-tube vedios to get a idea about Linux Commands related to navigation, file handling, and permissions.
- Googled for unknown commands.
- I broke out the problem into individual checks and tested each block.
- Used `echo` and `if-else` blocks to validate system behavior step by step.
  
  **Script:**
- [light_1](./soft_mars.sh)
- [light_2](./light_2nd.sh)

---

### 🟡 **Medium Dose**

#### 🔹 Question 1: Marker Navigation
- Wrote a function to decode directions from grid markers.
- Used matrix manipulation to simulate rover movement.

**Challenges Faced:**
- Navigating a 2D grid based on encoded markers.
- Avoiding index out-of-bound errors during movement.

**My Approach:**
- Represented the map as a matrix and simulated movements based on marker instructions.
- Implemented boundary checks and unit tests for each move.

---

#### 🔹 Question 2: Morse Decoder
- To get information about morse code for alphabets and numbers i used chatgpt.
- Built a Morse-to-text dictionary.
- Traversed through input and got corresponding decoded character from dictionary.
- It can give u decoded msg for big paragraphs witten in morse also.

 **Script:**
- [medium-2](./medium_1st.py)


#### 🔹 Question 3: Encrypted Message Decoding
- THE Logic was the characters shifted back according to its postion in the word
- Devoloped a code for it.
  
   **Script:**
- [medium-3](./medium_3rd.py)

---

#### 🔹 Question 4: Data Filtering (Muchiko, Sanchiko, Hybrid)
- Implemented and compared three filtering strategies on noisy sensor data.
- Used standard deviation to compare between the filters.
- Two hybrid filters have been created.(refer to script below)
  

---

#### 🔹 Question 5: Euler to Martian 4D Orientation
- I used chatgpt to understand quaternion math and conversion logic.
- Understood the term "Gimbal Lock"
- Developed a code for it
- Verified results using sample angle inputs and quaternion libraries.


---

### 🔴 **Hard Dose**

#### 🔹 Problem 1: Obstacle Map & Shortest Path
- Studied the obstacle map and built a arena using matrix.
- I had
- Implemented BFS to find the shortest navigable path.

**Challenges Faced:**
- Reading the map accurately and maintaining grid coordinates.
- Implementing BFS in a way that handled obstacles efficiently.

**My Approach:**
- Used nested lists to model the obstacle grid.
- Applied BFS with a visited set to ensure optimal traversal.

---

#### 🔹 Problem 3: Behavior Tree Design
- Designed a behavior tree to model rover decisions in a A4 sheet.
- Used fallback and sequence nodes for clean logical flow.
- Understood the terms and wrote answer in paper.



---






