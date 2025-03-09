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

Source for checking the end of the string:
    by w3schools
    accessed March 9th 2025
    Title: "Python String endswith() Method"
    https://www.w3schools.com/python/ref_string_endswith.asp    

    We needed to be able to check if the end of the string ended with .csv, because
    we are prompting the user for the file name they want to input and the file
    needs to end with .csv (this is for error handling)
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
    print("Welcome to _____")
    while user_choice != -1:
        fileOutput = ""
        print("Option 1: Collect the nessisary datafiles from Job Vacancies file")
        print("Option 2: Collect the nessisary datafiles from Highest Education Level file")
        print("Option 3: Collect the nessisary datafiles from the file for the comparison between not working due to an illness to Job Vacancies question")
        print("Option 4: Take out all of the unnessasary data in the average commute time file")
        temp_user_choice = input("Enter 1, 2, 3, 4, or -1 to exit: ")
        if (temp_user_choice.isdigit()):
            user_choice = int(temp_user_choice)
        else:
            print("*Error* Please enter only the number for each option i.e. either 1, 2, 3, or -1 to exit", file = sys.stderr)
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
            print("*Error* Unrecognised option, please enter one of the specified options above.")

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
                print("%s,%s,%s,%s,%s,\"Total - Highest certificate, diploma or degree\",\"No certificate, diploma or degree\",\"High (secondary) school diploma or equivalency certificate\","
                "\"Postsecondary certificate, diploma or degree\",\"Postsecondary certificate or diploma below bachelor level\",\"Apprenticeship or trades certificate or diploma\",\"Non-apprenticeship trades certificate or diploma\","
                    "\"Apprenticeship certificate\",\"College, CEGEP or other non-university certificate or diploma\",\"University certificate or diploma below bachelor level\","
                    "\"Bachelor’s degree or higher\",\"Bachelor's degree\",\"University certificate or diploma above bachelor level\",\"Degree in medicine, dentistry, veterinary medicine or optometry\","
                    "\"Master's degree\",\"Earned doctorate\"" 
                % (ref_Date, geo, statistics, age, sex), file = fileOutput)
            elif (statistics == stats):
                if(age == desiredAge):
                    if (sex == desiredSex):
                        print(f"{ref_Date},{geo},{statistics},{age},{sex},{educationLevel[0]},{educationLevel[1]}, {educationLevel[2]},{educationLevel[3]},{educationLevel[4]},{educationLevel[5]},{educationLevel[6]},"
                                f"{educationLevel[7]},{educationLevel[8]},{educationLevel[9]},{educationLevel[10]},{educationLevel[11]},"
                                f"{educationLevel[12]},{educationLevel[13]},{educationLevel[14]},{educationLevel[15]}" , file = fileOutput)
                                    
                            # elif(educationLevel == "No certificate, diploma or degree"):
                            #     print("%s,%s,%s,%s,\"No certificate, diploma or degree\",%s,%s" % (ref_Date, geo, statistics, sex, UOM, value), file = fileOutput)
                            # elif(educationLevel == "College, CEGEP or other non-university certificate or diploma"):
                            #     print("%s,%s,%s,%s,\"College, CEGEP or other non-university certificate or diploma\",%s,%s" % (ref_Date, geo, statistics, sex, UOM, value), file = fileOutput)
                            # else:
                            #     print("%s,%s,%s,%s,%s,%s,%s" % (ref_Date, geo, statistics, sex, educationLevel, UOM, value), file = fileOutput)
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

main()
# Call functions
#   End of Script