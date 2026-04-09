# Mars_Task-1

## Light dose 
### Ubuntu terminal commands

rover_commands.sh file contains the bash script containing all commands
` mkdir ` this creates a new directory in it
` cd ` goes into that directory
` touch ` it creates new files in the current dir
` mv ` it is to move a file to other file or to rename a files
` find . -type f -name "name" ` it will search for the files with that name in the current directory
` cat ` this displays the content in the file
` grep "word" "file" ` This will print the lines with the word in the given file
` wc -l ` will give no of lines
` date ` will give you the date time in terminal
` top ` will give you the system performance window
` shutdown +10 ` will shoutdown the laptop in 10 sec.

Resources: https://www.geeksforgeeks.org/linux-commands-cheat-sheet/

### Bash Scripting

rover_system_check.sh file contains this bash scripting
- This will store that log at "rover_log.txt".
- This will create random battery percentage if it is lower than 20 it will print Battery low. it will go to google.com and check the pig if it is 0 then it will print communication failure. If there is no problem then it will print "All systems operational"

approach: Framed the logic and then researched about the command and wrote the code.
Resources: https://devhints.io/bash, Google search.

## Medium Dose
### CODING(C,C++,Python)

File: obj_cor.py
Formula used: 
- degree to radian: angle x pi/180
- Rotation around x axis : 1) y = ycos(x) - xsin(x) 2) z = ysinx + xcosx 3) x = x
- Rotation around y axis : 1) x = xcos(y) - zsin(y) 2) z = -xsiny + zcosy 3) y = y
- Rotation around z axis : 1) x = xcos(z) - ysin(z) 2) z = xsinz + ycosz 3) z = z

We are rotating the point first and translating.

Approaches: learned about the formulas from google and searched for fuctions in python libraris

Resouces used: https://www.w3schools.com/python/, google search.

### Decoding Morse Code

File: morse_decode.py
Found a dictionary of letters in Chatgpt and wrote decode funtion.

Approach: Learned about morse code first and then used the algo to decode.

Resources used: https://en.wikipedia.org/wiki/Morse_code#:~:text=Morse%20code%20is%20a%20telecommunications,several%20developers%20of%20the%20system., chatgpt, https://www.w3schools.com/python/.

### Decrypting message from rover

File: rover_decrypt.py
splitted every word and letter and decrypted evry letter and join them.

Approach: Used python code to split every letter and going to previous letter according to the letters position in the given text. 

Challenges faced:
- tried to use ` range(word) ` but later came to know we should use ` range(len(word)) `.

Resources used: https://www.w3schools.com/python/.
### Question - 4

File: filter.py
we need to use 2 algorithem given in the question to to filter the data. 

Approach: Understood the given algorithem and implemented in python code by seaching for algorithems relevent to that in google.

challenges faced:
- to take input as list don't know how to take, used chatgpt for the function. It gave the one i used in the code. I understood what the map function do which i am not familiar with.

Resources used: https://www.w3schools.com/python/ ,Chatgpt.

### 5)Exciting News from Mars to MaRS!

File: configuration.py

used the given algorithems like cost

Approach: Understood the problem and constraints to solve the problem

Challenges faced: 
- Took help to understand the question from chatgpt. 

resources used: https://www.w3schools.com/python/, chatgpt.

## Hard Dose:
### 1)Task
File: guide_rover_brick.py

used algo: x coordinage = east - west
            y coordinate = north - south
        
challenges faceed: used chatgpt and stackoverflow to solve some python errors.

Resources used: stackoverflow, https://www.w3schools.com/python/, chatgpt.

### 2)Task

File: arrow_distance.py

Challenges facedd: 
- Learned about Pinhole camera
- learning nupy and cv2
- took help of chatgpt for understanding the code and question.

Resources used: stackoverflow, https://numpy.org/doc/, https://www.w3schools.com/python/numpy/default.asp,, https://docs.opencv.org/4.x/d1/dfb/intro.html, chatgpt.