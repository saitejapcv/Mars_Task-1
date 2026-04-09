#!/bin/bash

LOG_FILE="rover_log.txt" # Every ouptut we get is stored in Log file

battery=$(( RANDOM % 101)) # It will choose a number from 1-100 randomly
echo "Battery Lever = $battery%" | tee -a $LOG_FILE # tee will print this in terminal and append to log file

if [ $battery -lt 20 ]; then 
	echo "Battery low! Return to Base!" | tee -a $LOG_FILE # This prints the text if the battery level is less than 20
	exit 1
fi

ping -c 1 google.com > /dev/null 2>&1 # It checks the ping

if [ $? -ne 0 ]; then # the expression means if last statement is not equal to 0 then
	echo "Communication Falure!" | tee -a $LOG_FILE #This prints the text if ping is not equal to 0
	exit 1;
fi

echo "All systems operational!" | tee -a $LOG_FILE # This prints the text if it is not exited which means no error.
