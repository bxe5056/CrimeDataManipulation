# CrimeDataManipulation
This python 3 program is a hodgepodge of CSV manipulation techniques. 

Run from Command Line or powershell (python3 plot.py)

On Start, input the filename of the CSV file you want to work with. Everything must be in the same folder as the python (plot.py) file.
(Typing the filename is not mandatory for some of the non-file-specific functions described later)

General Program Layout: (To initiate a certain function, type y, otherwise press any other key and press enter

Count of the Cells in a Specific Column (Filename: REQUIRED)
You will select a column number of the specific field you want counted. 
Sample Output (txt) (filename_Count[type].txt)
ABAND/INOPERATIVE VEHICLE/CC~ 596 
ABET ENT/REM ON PREM~ 26 
ABUSE/NEG OF ADULTS~ 1 
ACC AFTER FACT(Code Modifier)~ 74 
ACCESS DEVICE FRAUD~ 1491 

Make Geocode Files (Filename: REQUIRED)
You will select the Address, City, State, & Zip Code of the CSV you would like Geocoded
All Fields are required, however the city, state, and Zip Code can be manually entered if they are static and consistent across all records.
You must type in a New Folder Name to store the broken CSV's.
Set uniqueID to a number < 1000. (This is how many rows are in each broken/part file. The Census geocoding system cannot handle more than 1000 records at a time.)
The function will break apart the main CSV file, and output multiple files into the newly created folder.
You will have the option to submit the files directly to the Census for Geocoding. Skip to the next function.
Digitally Geocode Files (Work in Progress) (Filename: Not Required) (Only accessible on a UNIX machine)
Select if you'd like to submit all CSV files in the current folder. (Ex. A Make Geocode Folder)
If yes, 
All CSV files in the folder are submitted. One after the other. If coming directly from Make Geocode Files, there will be a count under each submission. Otherwise it will show the number of files completed.
If no,
     Type the single filename you want to submit. 
If you receive Errno 17, rename the out folder.
Function will query the Census and return results.
If you wish to recombine the part/broken files, press y at 'Combine CSV Files'. The file will be located in the squish folder inside the out folder.
Combine CSV Files in current dir (Filename: Not Required)
This function takes all CSV files in random order and merges them into one CSV in a newly created 'squish' folder.
Make one Column CSV (Filename: REQUIRED)
Outputs one Complete Column from the Main CSV file.
Drop rows that do not meet specified criteria.
Separates a CSV by Year. Input the Year you would like results on and the function will return an individual CSV file with only your criteria.. 
      Are you done?
The program can loop for multiple files or functions without reopening the program.
If selected, you are asked if you need to switch to a different main file. 
The program will then repeat in the same order as above.
