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
 
 
 #
 # Define any "constants" for the file here.
 # Names of constants should be in UPPER_CASE.
 #
 
'''
 References:
 https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410037101
 https://www150.statcan.gc.ca/n1/daily-quotidien/240826/t003a-eng.htm 
 https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=9810038601 
 https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310089101&cubeTimeFrame.startYear=2017&cubeTimeFrame.endYear=2022&referencePeriods=20170101%2C20220101 
'''
def main():
    lineNumber = 0
    print("Welcome to _____")
    while True:
        print("Option 1: Do job vacancies affect the average commute time across the provinces?")
        print("Do regions with lower education levels have differing job vacancy rates compared to regions with higher education rates?")
        print("What is the correlation between people with disabilities who are unable to find work and the amount of job vacancies?")
        user_choice = input("Enter 1, 2, 3, or -1 to exit:")
        if user_choice == -1:
            break
        elif user_choice == 1:
            commute()
        elif user_choice == 2:
            education()
        elif user_choice == 3:
            disabilites()
 
     #   End of Function
 
def commute():
     #Collecting the data file
    dataFile = "../original_data_files/Average_Commute_Time.csv"
    try:
        dataFile_fh = open(dataFile, encoding = "utf-8-sig")
    except TypeError:
        print("*Error* could not open file\n %s\n please enter a different file" % (dataFile), file = sys.stderr())
        sys.exit(1)
    dataFile_reader = csv.reader(dataFile_fh)
 
     #looping through the entire data file to print the needed feilds into a different file
    for rowDataFeilds in dataFile_reader:
        REF_DATE = rowDataFeilds[0]    
        GEO = rowDataFeilds[1]
def education():
    #Collecting the data file
    dataFile = "../original_data_files/Highest_Level_Of_Education.csv"
    try:
        dataFile_fh = open(dataFile, encoding = "utf-8-sig")
    except TypeError:
        print("*Error* could not open file\n %s\n please enter a different file" % (dataFile), file = sys.stderr())
        sys.exit(1)
    dataFile_reader = csv.reader(dataFile_fh)
 
     #looping through the entire data file to print the needed feilds into a different file
    for rowDataFeilds in dataFile_reader:
         REF_DATE = rowDataFeilds[0]    
         GEO = rowDataFeilds[1]
 
def disabilites():
  
     #Collecting the data file
    dataFile = "../original_data_files/Reasons_Not_Looking_For_Work.csv"
    try:
        dataFile_fh = open(dataFile, encoding = "utf-8-sig")
    except TypeError:
        print("*Error* could not open file\n %s\n please enter a different file" % (dataFile), file = sys.stderr())
        sys.exit(1)
    dataFile_reader = csv.reader(dataFile_fh)
 
     #looping through the entire data file to print the needed feilds into a different file
    for rowDataFeilds in dataFile_reader:
        REF_DATE = rowDataFeilds[0]    
        GEO = rowDataFeilds[1]
        reason = rowDataFeilds[4]
        estimates = rowDataFeilds[5]
        UOM = rowDataFeilds[6]
        value = rowDataFeilds[12]
 
        if (reason == "Total, not in the labour force" or reason == "Wanted work, reason - illness" or reason == "Not in the labour force and did not want work or not available"):
            if (estimates == "Number of persons"):
                if (UOM == "Number"):
                    print("%s,%s,%s,%s,%s,%s" % (REF_DATE, GEO, reason, estimates, UOM, value))
 
 
 # Call functions
main()
 
 
 #   End of Script