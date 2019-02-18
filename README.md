# ImageDistraction
Welcome to the Image Distraction Github library! Here we offer programs that use images to distract Red Team by constantly opening them. Currently we have a Python file made for Windows that can be placed onto a Windows box that has python and ran to open up images constantly to distract the Blue Team so you can do other stuff!

How to Use: Upload ImageDistractionWin.py to Windows or ImageDistractionLinux.sh(NOT AVAILABLE YET) to the box you want to attack with it. Once it is there, simply run the script and watch as images randomly pop up, forcing blue team to waste precious time dealing with this mess.

Details: Works on Windows 7 and 10 provided they have Python!

Imagedistraction uses the user of the current user running the program, it grabs images from the user's pictures folder from either Windows or Linux(depending on which you grab). And than will open up roughly 25 to 200 images with 1 to 5 second intervals inbetween.

Usage Warnings: 
  1. The Program must be uploaded to the intended computer and than ran, no command line arguements are necessary.
  2. Pictures must be uploaded to the Pictures directory or the program will fail. 

Note: Image Distraction Win.py Only works for Windows and will also only function if Python is on the machine it is running on. Please be careful with that knowledge.

Futureworks: I will be working on creating a Bash script to run on Linux that will do the same as the Windows Python script. 
