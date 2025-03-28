import sys
import csv
from pathlib import Path
'''
Author(s):  Wyatt Evans 1293147, Harveen Harveen 1337280, Indigo Asher 1348315

Project: Milestone III
Date of Last Update: March 23rd 2025

Functional Summary
    This file calls a few files, that are given in the original_data_files folder and collects only the nessasary information
    that is required to answer our questions that were made in Milestone I

    When collecting the files that will take in the nessasary data the code goes to the current working directory (The one this file is in)
    then leaves this file, to go find the corrisponding file that is needed to collect the data for the option chosen by the user

'''


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
    canada = "Canada"
    #looping through the entire data file to print the needed feilds into a different file
    for row_data_fields in dataFile_reader:
        if (row_data_fields):
            ref_Date = row_data_fields[0]    
            geo = row_data_fields[1]
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
                print("%s, Education Level, Value"% (geo), file = fileOutput)
            elif (statistics == stats):
                if(age == desiredAge):
                    if (sex == desiredSex):
                        if(geo == "Canada" or geo == "Newfoundland and Labrador" or geo == "Prince Edward Island" or geo == "Nova Scotia" or
                           geo == "New Brunswick" or geo == "Quebec" or geo == "Ontario" or geo == "Manitoba" or geo == "Saskatchewan" or
                           geo == "Alberta" or geo == "British Columbia" or geo == "Yukon" or geo == "Northwest Territories" or geo == "Nunavut"):
                        
                            print(f"{geo},\"Total - Highest certificate, diploma or degree\",{educationLevel[0]}\n"
                                    f"{geo},\"No certificate, diploma or degree\",{educationLevel[1]}\n"
                                    f"{geo},\"High (secondary) school diploma or equivalency certificate\",{educationLevel[2]}\n"
                                    f"{geo},\"Postsecondary certificate, diploma or degree\",{educationLevel[3]}\n"
                                    f"{geo},\"Postsecondary certificate or diploma below bachelor level\",{educationLevel[4]}\n"
                                    f"{geo},\"Apprenticeship or trades certificate or diploma\",{educationLevel[5]}\n"
                                    f"{geo},\"Non-apprenticeship trades certificate or diploma\",{educationLevel[6]}\n"
                                    f"{geo},\"Apprenticeship certificate\",{educationLevel[7]}\n"
                                    f"{geo},\"College, CEGEP or other non-university certificate or diploma\",{educationLevel[8]}\n"
                                    f"{geo},\"University certificate or diploma below bachelor level\",{educationLevel[9]}\n"
                                    f"{geo},\"Bachelor’s degree or higher\",{educationLevel[10]}\n"
                                    f"{geo},\"Bachelor's degree\",{educationLevel[11]}\n"
                                    f"{geo},\"University certificate or diploma above bachelor level\",{educationLevel[12]}\n"
                                    f"{geo},\"Degree in medicine, dentistry, veterinary medicine or optometry\",{educationLevel[13]}\n"
                                    f"{geo},\"Master's degree\",{educationLevel[14]}\n"
                                    f"{geo},\"Earned doctorate\",{educationLevel[15]}" , file = fileOutput)

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
            print("%s,%s,%s,%s" % (ref_Date, geo, reason, value), file = fileOutput)

        
        if (estimates == numOfPeople):
            if (UOM == UOM_Expected):
                if(value):
                    if (reason == total):
                        print("%s,%s,\"Total, not in the labour force\",%s" % (ref_Date, geo, value), file = fileOutput)
                    elif(reason == ilness):
                        print("%s,%s,\"Wanted work , reason - illness\",%s" % (ref_Date, geo, value), file = fileOutput)
                    elif(reason == notAble):
                        print("%s,%s,%s,%s" % (ref_Date, geo, reason, value), file = fileOutput)
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
            if ("2017" in ref_Date or "2021" in ref_Date or "2022" in ref_Date or "2023" in ref_Date or "2024" in ref_Date):
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
            print(f"GEO,Year,VALUE", file = fileOutput)
        elif lineNumber in range (3,14):
            ref_date = rowDataFeilds[0]    
            commuteTime.append(rowDataFeilds[1])
            commuteTime.append(rowDataFeilds[2])
            commuteTime.append(rowDataFeilds[3])
            commuteTime.append(rowDataFeilds[4])
            commuteTime.append(rowDataFeilds[5])
            print(f"{rowDataFeilds[0]},{year[1]},{commuteTime[1]}\n{rowDataFeilds[0]},{year[2]},{commuteTime[2]}\n"
                  f"{rowDataFeilds[0]},{year[3]},{commuteTime[3]}\n{rowDataFeilds[0]},{year[4]},{commuteTime[4]}", file = fileOutput)
           
        lineNumber += 1
        commuteTime.clear()

# Call functions
#   End of Script