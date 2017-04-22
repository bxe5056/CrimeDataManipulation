import sys
import os
import csv
import time

#GLOBAL VARIABLES
file_Count_Geo = 1

def saveWords(wordfreq, current_file): #Function to save wordCounts to a file
    fileName_splitA, fileExt = os.path.splitext(current_file)
    #Get User Data Type
    print('Type of Data?: ')
    dataType = input()
    #Concatenate Data Type into Output File Name
    countFile = str(fileName_splitA) + "_Count" + str(dataType) + str('.txt')

    #Create or Open Output for Writing
    open(countFile, 'w')
    with open(countFile,'a') as file_output:
        for key in sorted(wordfreq.keys()): #Sort the Keys alphaNum and iterate over all keys
            file_output.write( "%s~ %s \n" % (key, wordfreq[key]) ) #Write Keys and Counts in Format '01/01/2001~ 999'
        print("  Word frequencies have been sorted.\n")
    print("  Frequencies have been saved in: '" + countFile + "'")

def getHeaders(filename): #Function to Retrieve CSV Header Row and output to Command Line
    with open(filename, newline='') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for i in range(1):
            newLines = []
            for line in next(reader):
                myList = line.split(",")
                newLines.append(myList)
        elemCount = 0
        for elem in newLines:
            print(elemCount,'=',elem)
            elemCount = elemCount + 1
        return newLines

def countDate(filename):
    datefreq = {}
    print('')
    getHeaders(filename)
    with open(filename, newline='') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        print('Select Column to count (Hint: First Column is 0)')
        rowNum = input()
        if rowNum is '`':
            print("           ***ESCAPE CHARACTER ENTERED***")
            print("            ***RETURNING TO MAIN MENU***\n")
            return
        rowNum = int(rowNum)
        for row in reader:
            date = str(row[rowNum])
            date = date.replace(u'\xc2', u' ') #Needed for SanFrancisco to process without error
            print(date)
            if date not in datefreq:
                datefreq[date] = 0
            datefreq[date] += 1
    print('')
    print(datefreq)
    print('')
    saveWords(datefreq, filename)

def oneColumn(filename):
    datefreq = {}
    print('')
    getHeaders(filename)
    with open(filename, newline='') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        print('Select Column to count (Hint: First Column is 0)')
        rowNum = input()
        if rowNum is '`':
            print("           ***ESCAPE CHARACTER ENTERED***")
            print("            ***RETURNING TO MAIN MENU***\n")
            return
        rowNum = int(rowNum)
        fileName_splitA, fileExt = os.path.splitext(filename)
        countFile = str(fileName_splitA) + "_OneCol" + str(rowNum) + str('.txt')
        print("Are we making dates with no times?:")
        print('    y/n?: ')
        goToSwitch = input()
        if goToSwitch is 'y':
            open(countFile, 'w')
            with open(countFile,'a') as file_output:
                for row in reader:
                    string = str(row[rowNum])
                    string = string[0:10]
                    file_output.write(string+'\n')
                    #print(string) #Omitted to save time...
        else:
            open(countFile, 'w')
            with open(countFile,'a') as file_output:
                for row in reader:
                    file_output.write(str(row[rowNum])+',')
                    print(str(row[rowNum])+',')
        print('')

def MaxVal(filename): #FUNCTION DISABLED DUE TO NON-USE
    datefreq = {}
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        for i in range(1):
            print(next(reader))
    with open(filename, newline='') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        print('Select Column (Hint: First Column is 0)')
        rowNum = int(input())
        for row in reader:
            CurrentValue = str(row[rowNum])
            print(CurrentValue)
            if CurrentValue > MaxValue:
                MaxValue = CurrentValue
        #Export result to txt File
        fileName_splitA, fileExt = os.path.splitext(current_file)
        countFile = str(fileName_splitA) + "_Count" + str('.txt')
        open(countFile, 'w')
        with open(countFile,'a') as file_output:
            file_output.write("The Maximum Value in the column is: " + MaxValue )
    print('')
    print('')
    saveWords(datefreq, filename)

def dropRows(filename): #Function to Filter a CSV by Year
    import re
    import csv
    import argparse
    import csv
    import sys
    import time
    #Display Headers of Input
    print('')
    getHeaders(filename)
    #Determine what column holds date information
    with open(filename, newline='') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        #Determine what column holds date information
        print('\nSelect Column to count (Hint: First Column is 0)')
        rowNum = input()
        if rowNum is '`':
            print("           ***ESCAPE CHARACTER ENTERED***")
            print("            ***RETURNING TO MAIN MENU***\n")
            return
        rowNum = int(rowNum)
        #Determine what year to filter by
        print("Please input Year to retrieve(YYYY): ")
        yearSelect = int(input())
        #Generate Output File Name
        fileName_splitA, fileExt = os.path.splitext(filename)
        outputFileName = str(fileName_splitA) + "_" + str(yearSelect) + "Filtered" + str(rowNum) + str('.txt.csv')
        open(outputFileName, 'w')
        with open(outputFileName, 'w', newline='') as file_output:
            wr = csv.writer(file_output, quoting=csv.QUOTE_ALL)
            isRowOne = 1 #Needed to ensure Header carryover from input to output
            for row in reader:
                row=[item.replace('\n', ', ') for item in row] #Remove any unneccesary Line Breaks
                rowTemp = row #Temporarily Hold Entier Row in Memory
                #print(rowTemp) #DEBUG
                yearTest = str(row[rowNum])
                yearTest = yearTest[6:10]
                yearTest = re.sub("[^0-9]", "", str(yearTest)) #Remove any extra characters from yearTest
                yearSelect = re.sub("[^0-9]", "", str(yearSelect)) #Remove any extra characters from yearSelect
                if yearTest == yearSelect:
                    print(rowTemp)
                    wr.writerow(rowTemp)
                if isRowOne == 1:
                    print(rowTemp)
                    wr.writerow(rowTemp)
                    isRowOne = 2
    #Module Completed
    print('')
    print('Returning to Main Menu...')
    print('3...')
    time.sleep(1)
    print('2...')
    time.sleep(1)
    print('1...')
    time.sleep(1)
    print('')

def exitCall():
    print('Are you done?')
    print('  y/n?: ')
    exitSwitch = input()
    if exitSwitch is 'y':
        print('3...')
        time.sleep(1)
        print('2...')
        time.sleep(1)
        print('1...')
        time.sleep(1)
        print('Goodbye!')
        return 'break'
    else:
        if os.name == 'nt':
            os.system('cls')  # for Windows
        else:
            os.system('clear')  # for Linux/OS X

def curlGeo(filename):
    welcome = 'Welcome to the Geocoding Service. \n This feature will attempt to geocode your csv files in ~1,000 line chunks through the Census geocoding service. \n One thing to note when using this service is that input must conform to this format: Unique ID, Street Address, City, State, ZIP \n Any other format will be refused.'
    getStarted ="Let's get started"
    print(welcome)
    print(getStarted)
    getHeaders(filename)
    inputFormat = "Unique ID, Street Address, City, State, ZIP"
    uniqueID = 0
    addr = ""
    city = ""
    state = ""
    zip = 00000


    with open(filename, newline='') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        #UniqueID Generation
        print("Unique ID is automatically generated. It cannot ever exceed 1000.")
        #Address Col Generation
        print('\nSelect Column to to use as "Address" (Hint: First Column is 0)')
        col_addr = input()
        if col_addr is '`':
            print("           ***ESCAPE CHARACTER ENTERED***")
            print("            ***RETURNING TO MAIN MENU***\n")
            return
        col_addr = int(col_addr)
        #City Col Generation
        print("Is the City Consistant Across all Values (Type: y ), or is it controlled by a column in CSV?")
        cityCheck = input()
        if(cityCheck == 'y'):
            print("What is the value?: ")
            default_city = input()
            print("State Abbreviation: ")
            default_State = input()
            print("Zip Code: ")
            default_zip = input()
        else:
            print('\nSelect Column to to use as "City" (Hint: First Column is 0)')
            col_city = input()
            if col_city is '`':
                print("           ***ESCAPE CHARACTER ENTERED***")
                print("            ***RETURNING TO MAIN MENU***\n")
                return
            col_city = int(col_city)
            print('\nSelect Column to to use as "State" (Hint: First Column is 0)')
            col_State = input()
            if col_State is '`':
                print("           ***ESCAPE CHARACTER ENTERED***")
                print("            ***RETURNING TO MAIN MENU***\n")
                return
            col_State = int(col_State)
            print('\nSelect Column to to use as "Zip" (Hint: First Column is 0)')
            col_ZIP = input()
            if col_ZIP is '`':
                print("           ***ESCAPE CHARACTER ENTERED***")
                print("            ***RETURNING TO MAIN MENU***\n")
                return
            col_ZIP = int(col_ZIP)
    with open(filename, newline='') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        print("New Dir: ")
        newDir = input()
        os.mkdir(newDir)

        countFile = 1
        firstRow = 0

        outFile = filename + "." + str(countFile) + ".csv" #NEED TO FIX WITH CONCAT CODE
        outFile = str(newDir) + str("/" + outFile)
        out = open(outFile, 'w')

        print("uniqueID should be set to what number under 1000?: ")
        instanceUID = input()
        instanceUID = int(instanceUID)

        for row in reader:
            if firstRow != 0:
                if uniqueID < instanceUID:
                    if cityCheck != 'y':
                        addr = str(row[col_addr])
                        city = str(row[col_city])
                        state = str(row[col_State])
                        zip = str(row[col_ZIP])
                    else:
                        addr = str(row[col_addr])
                        city = str(default_city)
                        state = str(default_State)
                        zip = str(default_zip)
                    row_out = ""
                    if addr != '':
                        uniqueID = uniqueID + 1
                        row_out = str(uniqueID) + ', "' + addr + '", "' + city + '", "' + state + '", ' + zip +'\n'
                        out.write(row_out)
                    print(row_out)
                else:
                    out.close()
                    countFile = countFile + 1
                    outFile = filename + "." + str(countFile) + ".csv" #NEED TO FIX WITH CONCAT CODE
                    outFile = str(newDir) + str("/" + outFile)
                    out = open(outFile, 'w')
                    uniqueID = 0
                    global file_Count_Geo
                    file_Count_Geo = file_Count_Geo + 1
            firstRow = 1

        print("Are we Processing Today?: y/n: ")
        goToSwitch = input()
        if goToSwitch is 'y':
            getGeo(filename,newDir)

def getGeo(filename,newDir):
    #DISABLED DUE TO REQUIRING JAVASCRIPT TO CURL
    #Not Really, I reenabled it. But it only works on UNIX distros.
    #Until this is fixed, user must use linux bow w/ cURL to geocode manually.

    import glob
    from sys import platform as _platform
    if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
        # linux or OSX
        print("Are we doing all files in Directory?: y/n")
        getAllFiles = input()
        countFile = 1
        if getAllFiles == 'y':
            if newDir != '':
                os.chdir(newDir)
            os.mkdir('out')
            for files in glob.glob("*.csv"):
                command = 'curl --form addressFile=@' + files +' --form benchmark=9 -k https://geocoding.geo.census.gov/geocoder/locations/addressbatch --output out/' + files + 'out.csv'
                os.system(command)
                print(str(countFile) + ' of '+ str(file_Count_Geo) +'...')
                countFile = countFile + 1

            print("Squish?: y/n")
            squishCheck = input()
            if squishCheck == 'y':
                os.chdir(out)
                os.mkdir('squish')
                outFile = open('squish/ALL.csv', 'w')
                for files in glob.glob("*.csv"):
                    cf = open(files, 'r')
                    for row in cf:
                        outFile.write(row)
        else:
            print("Single Filename: ")
            fileoperating = input()
            command = 'curl --form addressFile=@' + fileoperating +' --form benchmark=9 -k https://geocoding.geo.census.gov/geocoder/locations/addressbatch --output ' + fileoperating + 'out.csv'
            os.system(command)

    elif _platform == "win32":
        print("ERROR: This module can only be run from a UNIX machine.")
        # Windows...
    '''
    #os.system('curl --form addressFile=@localfile.csv --form benchmark=9 -k https://geocoding.geo.census.gov/geocoder/locations/address' )
    import requests
    import json
    url = 'https://geocoding.geo.census.gov/geocoder/locations/address'
    print("File Me!: ")
    inputFile = input()
    headers = {'Content-Type': 'application/json'}
    payload = {'benchmark': '9'}
    files = {'addressFile': open(inputFile, 'r')}
    r = requests.get(url, files=files, headers=headers, data=payload, verify=False )
    with open("code3.csv", "wb") as code:
        code.write(r.content)
    '''

def combineCSV():
    import glob
    os.mkdir('squish')
    outFile = open('squish/ALL.csv', 'w')
    for files in glob.glob("*.csv"):
        cf = open(files, 'r')
        for row in cf:
            outFile.write(row)


#MAIN
print("Filename of CSV Input: ")
filename = input()
while True: #Controlled by #ExitCode
    #Print Program  Options
    print('')
    print('General Program Layout is:')
    print('  Count of Cells in a Column -> Output ')
    print('    y/n?: ')
    goToSwitch = input()
    if goToSwitch is 'y':
        countDate(filename)
    #MaxValueFunction has been disabled as it is not used often
    #print('  Max Value of Cells in a Column -> Output ')
    #print('    y/n?: ')
    #goToSwitch = input()
    #if goToSwitch is 'y':
    #    MaxVal(filename)

    #MinValueFunction has been disabled as it is not used often
    #print('  Min Value of Cells in a Column -> Output ')
    #print('    y/n?: ')
    #goToSwitch = input()
    #if goToSwitch is 'y':
    #    MinVal(filename)

    print('  Make Geocode Files ')
    print('    y/n?: ')
    goToSwitch = input()
    if goToSwitch is 'y':
        curlGeo(filename)

    print('  Digitally Geocode Files ')
    print('    y/n?: ')
    goToSwitch = input()
    if goToSwitch is 'y':
        getGeo(filename)

    print('  Combine CSV Files in currect dir')
    print('    y/n?: ')
    goToSwitch = input()
    if goToSwitch is 'y':
        combineCSV()

    print('  Make one Column CSV -> Output ')
    print('    y/n?: ')
    goToSwitch = input()
    if goToSwitch is 'y':
        oneColumn(filename)

    print('  Drop rows that do not meet specified criteria -> Output.csv')
    print('    y/n?: ')
    goToSwitch = input()
    if goToSwitch is 'y':
        dropRows(filename)

    #Exit Code
    isDone = exitCall()
    if isDone is 'break':
        break

    print('The current file is',filename)
    print('  Do you need a different file? ')
    print('    y/n?: ')
    goToSwitch = input()
    if goToSwitch is 'y':
        print("Filename of CSV Input: ")
        filename = input()
