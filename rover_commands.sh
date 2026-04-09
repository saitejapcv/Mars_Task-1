#!/bin/bash

# Question 1 
mkdir -p rover_mission
cd rover_mission

# Question 2
touch log1.txt log2.txt log3.txt

# Question 3
mv log1.txt mission_log.txt

# Question 4
find . -type f -name "*.log"

# Question 5
cat mission_log.txt

# Question 6
grep "ERROR" mission_log.txt

# Question 7
wc -l mission_log.txt

# Question 8
date

# Question 9
top

# Question 10
shutdown +10
