#!/bin/bash

echo "Starting soft_mars Script..."

# 1. Create a new directory called rover_mission and navigate into it
mkdir -p rover_mission
cd rover_mission || exit

# 2. Create three empty files: log1.txt, log2.txt, and log3.txt
touch log1.txt log2.txt log3.txt

# 3. Rename log1.txt to mission_log.txt
mv log1.txt mission_log.txt

# 4. Find all files in the current directory with a .log extension
echo "Files with .log extension:"
find . -type f -name "*.log"

# 5. Display the contents of mission_log.txt without opening it in an editor
echo "Contents of mission_log.txt...."
cat mission_log.txt

# 6. Find and display all lines containing the word "ERROR" in mission_log.txt
echo "Lines containing 'ERROR' in mission_log.txt..."
grep "ERROR" mission_log.txt || echo "No 'ERROR' found."

# 7. Count the number of lines in mission_log.txt
echo "Number of lines in mission_log.txt..."
wc -l mission_log.txt | awk '{print $1}'

# 8. Show the system's current date and time
echo "Current Date and Time..."
date

# 9. Display the CPU usage of your system in real time
echo "CPU usage..."
top -bn1 | grep "Cpu(s)"

# 10. Schedule a command to shut down the system in 10 minutes
echo "to shutdown in 10 minutes"
sudo shutdown -h +10


