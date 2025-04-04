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

## **6. Task Breakdown**

###  **Light Dose**

#### 🔹 Question 1: Rover System Check
- Simulated a series of rover diagnostics using a Bash script.
- Used conditional statements and process outputs to mimic real-time behavior.

**Challenges Faced:**
- Debugging syntax errors and ensuring correct logical flow in the shell script.
- Handling command outputs for different system checks.

**My Approach:**
- Broke the problem into individual checks and tested each block.
- Used `echo` and `if-else` constructs to validate system behavior step by step.
**Script:** [light_2nd.sh](./light_2nd.sh)


---

#### 🔹 Question 2: Terminal-Based Rover Task
- Practiced common Linux commands related to navigation, file handling, and permissions.
- Reinforced shell scripting skills through real-world robotic context.

**Challenges Faced:**
- Remembering specific syntax for file and directory operations.
- Understanding permission errors and how to resolve them.

**My Approach:**
- Referred to Linux man pages and practiced each command in the terminal.
- Used `chmod`, `ls -l`, and `pwd` to verify operations and access rights.

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
- Created a Python script to translate Morse signals to readable messages.
- Handled edge cases like spacing and special characters.

**Challenges Faced:**
- Handling inconsistent spacing between Morse symbols.
- Managing unknown or invalid characters.

**My Approach:**
- Built a Morse-to-text dictionary.
- Split input based on spaces and iterated carefully through each symbol.

---

#### 🔹 Question 3: Encrypted Message Decoding
- Decoded a custom cipher using reverse logic.
- Developed a reusable decryptor function.

**Challenges Faced:**
- Understanding the shifting pattern used in encryption.
- Managing wrap-around cases in the alphabet.

**My Approach:**
- Reverse engineered the cipher by analyzing output patterns.
- Created a loop that decodes each character while preserving non-alphabet symbols.

---

#### 🔹 Question 4: Data Filtering (Muchiko, Sanchiko, Hybrid)
- Implemented and compared three filtering strategies on noisy sensor data.
- Evaluated the effectiveness of each in a simulated rover environment.

**Challenges Faced:**
- Choosing the right filter parameters.
- Understanding when each filtering method performs best.

**My Approach:**
- Wrote separate functions for each filter.
- Ran simulations with varied input sets and compared output accuracy.

---

#### 🔹 Question 5: Euler to Martian 4D Orientation
- Converted Euler angles to quaternions.
- Studied 4D orientation systems used in aerospace and robotics.

**Challenges Faced:**
- Understanding quaternion math and conversion logic.
- Ensuring numerical stability in calculations.

**My Approach:**
- Referred to aerospace math documentation.
- Verified results using sample angle inputs and quaternion libraries.

---

### 🔴 **Hard Dose**

#### 🔹 Problem 1: Obstacle Map & Shortest Path
- Parsed an obstacle map and built a matrix representation.
- Implemented BFS to find the shortest navigable path.

**Challenges Faced:**
- Reading the map accurately and maintaining grid coordinates.
- Implementing BFS in a way that handled obstacles efficiently.

**My Approach:**
- Used nested lists to model the obstacle grid.
- Applied BFS with a visited set to ensure optimal traversal.

---

#### 🔹 Problem 3: Behavior Tree Design
- Designed a behavior tree to model rover decisions.
- Used fallback and sequence nodes for clean logical flow.

**Challenges Faced:**
- Structuring the tree to handle edge cases and priorities effectively.
- Understanding how behavior trees differ from traditional conditional logic.

**My Approach:**
- Sketched the tree before coding to visualize the flow.
- Used modular functions to simulate node behavior and tree traversal.

---






