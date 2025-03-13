'''
Team_project.py

Author(s):  Wyatt Evans 1293147, Harveen Harveen 1337280, Mohamed Hendy 1332794, Indigo Asher 1348315

Project:
Date of Last Update:

Functional Summary
    
'''

#
#   Packages and modules
#

# The 'sys' module gives us access to system tools, including the
# command line parameters, as well as standard input, output and error
import sys

# The 'csv' module gives us access to a tool that will read CSV
# (Comma Separated Value) files and provide us access to each of
# the fields on each line in turn
import csv

from pathlib import Path

#
# Define any "constants" for the file here.
# Names of constants should be in UPPER_CASE.
#


'''
source for path:
    by geeksforgeeks
    accessed March 8th 2025
    Title:  "Find path to the given file using Python"
    https://www.geeksforgeeks.org/find-path-to-the-given-file-using-python/

    We needed to be able to access what the current working derectory is 
    in order to be able to access all of the nessasary files, and output 
    into the correct folder/right file

Source for clearing a list 
    by w3schools
    accessed: March 8th 2025
    Title: Python List clear() Method
    http://w3schools.com/python/ref_list_clear.asp

    We needed to clear the education level list, and the commuteTime list 
    so they don't print out the same values for each row

Source for checking the end of the string:
    by w3schools
    accessed March 9th 2025
    Title: "Python String endswith() Method"
    https://www.w3schools.com/python/ref_string_endswith.asp    

    We needed to be able to check if the end of the string ended with .csv, 
    because we are prompting the user for the file name they want to input 
    and the file needs to end with .csv (this is for error handling)

'''
'''
References:
https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410037101
https://www150.statcan.gc.ca/n1/daily-quotidien/240826/t003a-eng.htm 
https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=9810038601 
https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310089101&cubeTimeFrame.startYear=2017&cubeTimeFrame.endYear=2022&referencePeriods=20170101%2C20220101 
'''
def main():
    user_choice = 0
    path = str(Path.cwd())
    print("Welcome Please select which type of file you want to collect the nessasary data from")
    while user_choice != -1:
        fileOutput = ""
        print("Option 1: Collect the nessisary datafiles from Job Vacancies file")
        print("Option 2: Collect the nessisary datafiles from Highest Education Level file")
        print("Option 3: Collect the nessisary datafiles from the file for the comparison between not working due to an illness to Job Vacancies question")
        print("Option 4: Take out all of the unnessasary data in the average commute time file")
        temp_user_choice = input("Enter 1, 2, 3, 4, or -1 to exit: ")
        try:
            user_choice = int(temp_user_choice)
        except ValueError:
            print("\n\n*Error* Please enter only the integer (Whole Number) for each option i.e. either 1, 2, 3, or -1 to exit\n\n", file = sys.stderr)
            sys.exit(1)

        
        if user_choice == -1:
            print("\n\nExiting.......\n\n")
            break
        elif user_choice == 1:
            while(not fileOutput.endswith(".csv")):
                fileOutput = input("Please enter the file name you would like to print in: ")
                if(not fileOutput.endswith(".csv")):
                    print("*Error* This you did not enter a csv file")
            fileOutput = path + "/../../data_fields_from_data_files/" + fileOutput
            jobVacancies(fileOutput)

        elif user_choice == 2:
            while(not fileOutput.endswith(".csv")):
                fileOutput = input("Please enter the file name you would like to print in: ")
                if(not fileOutput.endswith(".csv")):
                    print("*Error* This you did not enter a csv file")
            fileOutput = path + "/../../data_fields_from_data_files/" + fileOutput
            education(fileOutput)

        elif user_choice == 3:
            while(not fileOutput.endswith(".csv")):
                fileOutput = input("Please enter the file name you would like to print in: ")
                if(not fileOutput.endswith(".csv")):
                    print("*Error* This you did not enter a csv file")
            fileOutput = path + "/../../data_fields_from_data_files/" + fileOutput
            disabilites(fileOutput)
        
        elif user_choice == 4:
            while(not fileOutput.endswith(".csv")):
                fileOutput = input("Please enter the file name you would like to print in: ")
                if(not fileOutput.endswith(".csv")):
                    print("*Error* This you did not enter a csv file")
            fileOutput = path + "/../../data_fields_from_data_files/" + fileOutput
            commute(fileOutput)

        else:
            print("\n\n*Error* Unrecognised option, please enter one of the specified options above.\n\n")

    #   End of Function

def education(fileOutput):
    rowNumber = 0
    educationLevel = []
    #Collecting the data file
    path = str(Path.cwd())
    dataFile = path + "/../../original_data_files/Highest_Level_Of_Education.csv"
    try:
        dataFile_fh = open(dataFile, encoding = "utf-8-sig")
        fileOutput = open(fileOutput, "w", encoding= "utf-8-sig")


    except TypeError:
        print("*Error* could not open file\n %s\n please enter a different file" % (dataFile), file = sys.stderr)
        sys.exit(1)

    dataFile_reader = csv.reader(dataFile_fh)
    
    #looping through the entire data file to print the needed feilds into a different file
    for row_data_fields in dataFile_reader:
        if (row_data_fields):
            ref_Date = row_data_fields[0]    
            geo = row_data_fields[1]
            geo = "\"" + geo + "\""
            statistics = row_data_fields[3]
            age = row_data_fields[4]
            sex = row_data_fields[5]
            educationLevel.append(row_data_fields[7])
            educationLevel.append(row_data_fields[9])
            educationLevel.append(row_data_fields[11])
            educationLevel.append(row_data_fields[13])
            educationLevel.append(row_data_fields[15])
            educationLevel.append(row_data_fields[17])
            educationLevel.append(row_data_fields[19])
            educationLevel.append(row_data_fields[21])
            educationLevel.append(row_data_fields[23])
            educationLevel.append(row_data_fields[25])
            educationLevel.append(row_data_fields[27])
            educationLevel.append(row_data_fields[29])
            educationLevel.append(row_data_fields[31])
            educationLevel.append(row_data_fields[33])
            educationLevel.append(row_data_fields[35])
            educationLevel.append(row_data_fields[37])

            UOM = row_data_fields[7]
            value = row_data_fields[13]

            stats = "Count"
            desiredSex = "Total - Gender"
            desiredAge = "Total - Age"

            if(rowNumber == 0):
                print("%s,%s,%s,%s,%s,\"No certificate, diploma or degree\",\"High (secondary) school diploma or equivalency certificate\","
                "\"All trades\",\"Postsecondary\"" % (ref_Date, geo, statistics, age, sex), file = fileOutput)
            elif (statistics == stats):
                educationLevel = [int(num) for num in educationLevel]

                noEd = educationLevel[1]
                secondaryEd = educationLevel[2]
                trades = educationLevel[5] + educationLevel[6] + educationLevel[7]
                # noEd = int(noEd)
                # trades = int(trades)
                # secondaryEd = int(secondaryEd)  
                postSecEd = educationLevel[0] - noEd - trades - secondaryEd
                if(age == desiredAge):
                    if (sex == desiredSex):
                        print(f"{ref_Date},{geo},{statistics},{age},{sex},{noEd},{secondaryEd}, {trades},{postSecEd}" , file = fileOutput)
        educationLevel.clear()
        rowNumber += 1
        

def disabilites(fileOutputLocation):
    path = str(Path.cwd())
    lineNumber = 0
    #Collecting the data file
    dataFile = path +  "/../../original_data_files/Reasons_Not_Looking_For_Work.csv"
    try:
        dataFile_fh = open(dataFile, encoding = "utf-8-sig")
        fileOutput = open(fileOutputLocation, "w", encoding= "utf-8-sig")
    except TypeError:
        print("*Error* could not open file\n %s\n please enter a different file" % (dataFile), file = sys.stderr)
        sys.exit(1)
    
    dataFile_reader = csv.reader(dataFile_fh)
    
    #looping through the entire data file to print the needed feilds into a different file
    for row_data_fields in dataFile_reader:
        ref_Date = row_data_fields[0]    
        geo = row_data_fields[1]
        reason = row_data_fields[4]
        estimates = row_data_fields[5]
        UOM = row_data_fields[6]
        value = row_data_fields[12]
        total = "Total, not in the labour force"
        ilness = "Wanted work, reason - illness"
        notAble = "Not in the labour force and did not want work or not available"
        numOfPeople = "Number of persons" 
        UOM_Expected = "Number"
        if (lineNumber == 0):
            print("%s,%s,%s,%s,%s,%s" % (ref_Date, geo, reason, estimates, UOM, value), file = fileOutput)

        
        if (estimates == numOfPeople):
            if (UOM == UOM_Expected):
                if(value):
                    if (reason == total):
                        print("%s,%s,\"Total, not in the labour force\",%s,%s,%s" % (ref_Date, geo, estimates, UOM, value), file = fileOutput)
                    elif(reason == ilness):
                        print("%s,%s\"Wanted work, reason - illness\",%s,%s,%s" % (ref_Date, geo, estimates, UOM, value), file = fileOutput)
                    elif(reason == notAble):
                        print("%s,%s,%s,%s,%s,%s" % (ref_Date, geo, reason, estimates, UOM, value), file = fileOutput)
        lineNumber += 1



#This file is to collect the needed data feilds from each data file
import sys
import csv
def jobVacancies(fileOutputLocation):
    lineNumber = 0
    path = str(Path.cwd())
    #Collecting the data file
    dataFile = path + "/../../original_data_files/Job_Vacancies.csv"
    try:
        dataFile_fh = open(dataFile, encoding = "utf-8-sig")
        fileOutput = open(fileOutputLocation, "w", encoding = "utf-8-sig")
    except TypeError:
        print("*Error* could not open file\n %s\n please enter a different file" % (dataFile), file = sys.stderr)
        sys.exit(1)
    dataFile_reader = csv.reader(dataFile_fh)

    #looping through the entire data file to print the needed feilds into a different file
    for row_data_fields in dataFile_reader:
        if (row_data_fields):
            
            ref_Date = row_data_fields[0]    
            geo = row_data_fields[1]
            statistics = row_data_fields[3]
            UOM = row_data_fields[4]
            value = row_data_fields[10]
            if(lineNumber == 0):
                print("%s,%s,%s,%s,%s" % (ref_Date, geo, statistics, UOM, value), file = fileOutput)
            #Check to see if the month is may
            if ("2021" in ref_Date or "2022" in ref_Date or "2023" in ref_Date or "2024" in ref_Date):
                if statistics == "Job vacancies":
                    if UOM == "Number":
                        if value:
                            print("%s,%s,%s,%s,%s" % (ref_Date, geo, statistics, UOM, value), file = fileOutput)
        lineNumber += 1

def commute(fileOutputLocation):
    path = str(Path.cwd())
     #Collecting the data file
    dataFile = path + "/../../original_data_files/Average_Commute_Time.csv"
    lineNumber = 0
    commuteTime = []
    year = []
    try:
        dataFile_fh = open(dataFile, encoding = "utf-8-sig")
        fileOutput = open(fileOutputLocation, "w", encoding = "utf-8-sig")
    except TypeError:
        print("*Error* could not open file\n %s\n please enter a different file" % (dataFile), file = sys.stderr())
        sys.exit(1)
    dataFile_reader = csv.reader(dataFile_fh)
 
     #looping through the entire data file to print the needed feilds into a different file
    for rowDataFeilds in dataFile_reader:
        if lineNumber == 1:
            year.append(rowDataFeilds[1])
            year.append(rowDataFeilds[2])
            year.append(rowDataFeilds[3])
            year.append(rowDataFeilds[4])
            year.append(rowDataFeilds[5])
            print(f"Geographical Location,{year[0]},{year[1]},{year[2]},{year[3]},{year[4]}", file = fileOutput)
        elif lineNumber in range (3,14):
            ref_date = rowDataFeilds[0]    
            commuteTime.append(rowDataFeilds[1])
            commuteTime.append(rowDataFeilds[2])
            commuteTime.append(rowDataFeilds[3])
            commuteTime.append(rowDataFeilds[4])
            commuteTime.append(rowDataFeilds[5])
            print(f"{ref_date},{commuteTime[0]},{commuteTime[1]},{commuteTime[2]},{commuteTime[3]},{commuteTime[4]}", file = fileOutput)
        lineNumber += 1
        commuteTime.clear()

main()
# Call functions
#   End of Script