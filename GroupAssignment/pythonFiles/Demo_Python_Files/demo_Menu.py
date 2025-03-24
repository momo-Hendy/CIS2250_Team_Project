'''
demo_Menu.py

Author(s):  Wyatt Evans 1293147, Harveen Harveen 1337280, Indigo Asher 1348315

Project: Milestone III
Date of Last Update: March 23rd 2025

Functional Summary
    File implements a menu to the project, allowing for user accesability. 
    Based on user decisions in the menu, call on 1 of 3 graph files and send which datafields they require.
    
    This file is the main section of our program, everything will link back to here.

    First it will prompt the user for 2 options:

    Option 1: Print Graph From Job Vaccancy Questions
    Option 2: Get Data From Files

    if they choose option 1 then they will be prompted for which question they want to answer, but if they haven't yet done then
    it will automaticly go to the one that is already made if it has been made then it will use that one.

    if they choose option 2 then they will be able to collect the data needed to create the graphs of option 1

'''

import sys
from pathlib import Path

import question1_Graph
import question2_Graph
import question3_Graph
import demo_Files

def main():
    user_choice = 0
    path = str(Path.cwd())

    #if varibales are empty, then preprocessing has not been done
    vacancies_location = "" 
    education_location = ""
    commute_location = ""
    disabilites_location = ""
    output_location = "" 
    user_choice = 0

    print("\nCIS2250-W25-Project Menu\n")
    while user_choice != -1:
        user_choice = 0
        user_choice2 = 0
        user_choice3 = 0

        fileOutput = ""
        print("\nOption 1: Print Graph From Job Vaccancy Questions")
        print("Option 2: Get Data From Files")
        try:
            temp_user_choice = input("Enter 1, 2, or -1 to exit: ")
        except ValueError:
            print("*Error* ")
        try:
            user_choice = int(temp_user_choice)
        except ValueError:
            print("\n\n*Error* Please enter only the integer (Whole Number) for each option i.e. either 1, 2, 3, or -1 to exit\n\n", file = sys.stderr)
            sys.exit(1)

        if user_choice == -1:
            print("\n\nExiting.......\n\n")
            break

        #assuming preprocessing has been completed, chose questions to turn into graphs
        elif user_choice == 1:
            print("\nChoose Question:")
           
            print("Option 1: Do job vacancies affect the average commute time across the provinces?")
            print("Option 2: Do regions with lower education levels have differing job vacancy rates compared to regions with higher education rates?")
            print("Option 3: What is the correlation between people with disabilities who are unable to find work and the amount of job vacancies?")
            print("Option -1: Return to main menu")
            temp_user_choice2 = input("Enter 1, 2, 3, or -1: ")
            try:
                user_choice2 = int(temp_user_choice2)
            except ValueError:
                print("\n\n*Error* Please enter only the integer (Whole Number) for each option i.e. either 1, 2, 3, or -1 to exit\n\n", file = sys.stderr)
                sys.exit(1)

            if user_choice2 == -1:
                print("")

            elif user_choice2 == 1:
                if vacancies_location == "":
                    vacancies_location =  path + "/../../data_fields_from_data_files/Job_Vacancies_Needed_Fields.csv"
                if commute_location == "":
                    commute_location = path + "/../../data_fields_from_data_files/Average_Commute_Time_In_Minutes.csv"

                output_location = "../../Output_Graphs/Question1/"#set output location 
                question1_Graph.question1_Graph(vacancies_location, commute_location, output_location)

            elif user_choice2 == 2:
                if vacancies_location == "":
                    vacancies_location =  path + "/../../data_fields_from_data_files/Job_Vacancies_Needed_Fields.csv"
                if education_location == "":
                    education_location = path + "/../../data_fields_from_data_files/Education_Level_Needed_Fields.csv"

                output_location = "../../Output_Graphs/Question2/" #set output location 
                question2_Graph.question2_Graph(vacancies_location, education_location, output_location)

            elif user_choice2 == 3:
                if vacancies_location == "":
                    vacancies_location =  path + "/../../data_fields_from_data_files/Job_Vacancies_Needed_Fields.csv"
                if disabilites_location == "":
                    disabilites_location = path + "/../../data_fields_from_data_files/Reasons_Not_Working_Needed_Fields.csv"

                output_location = "../../Output_Graphs/Question3/" #set output location 
                question3_Graph.question3_Graph(vacancies_location, disabilites_location, output_location)

            else:
                print("\n\n*Error* Unrecognised option, please enter one of the specified options above.\n\n")

        #get preprocessing from milestone II code
        elif user_choice == 2:
                    
            while user_choice3 != -1:
                fileOutput = ""
                print("Option 1: Collect the nessisary datafiles from Job Vacancies file")
                print("Option 2: Collect the nessisary datafiles from Highest Education Level file")
                print("Option 3: Collect the nessisary datafiles from the file for the comparison between not working due to an illness to Job Vacancies question")
                print("Option 4: Take out all of the unnessasary data in the average commute time file")
                temp_user_choice = input("Enter 1, 2, 3, 4, or -1 to return to main menu: ")
                try:
                    user_choice3 = int(temp_user_choice)
                except ValueError:
                    print("\n\n*Error* Please enter only the integer (Whole Number) for each option i.e. either 1, 2, 3, or -1 to exit\n\n", file = sys.stderr)
                    sys.exit(1)

                
                if user_choice3 == -1:
                    break
                elif user_choice3 == 1:
                    vacancies_location = input("Please enter the file name you would like to print in: ")
                    vacancies_location = path + "/../../data_fields_from_data_files/" + vacancies_location + ".csv"
                    demo_Files.jobVacancies(vacancies_location)

                elif user_choice3 == 2:
                    education_location = input("Please enter the file name you would like to print in: ")
                    education_location = path + "/../../data_fields_from_data_files/" + education_location + ".csv"
                    demo_Files.education(education_location)

                elif user_choice3 == 3:
                    disabilites_location = input("Please enter the file name you would like to print in: ")
                    disabilites_location = path + "/../../data_fields_from_data_files/" + disabilites_location + ".csv"
                    demo_Files.disabilites(disabilites_location)
                
                elif user_choice3 == 4:
                    commute_location = input("Please enter the file name you would like to print in: ")
                    commute_location = path + "/../../data_fields_from_data_files/" + commute_location + ".csv"
                    demo_Files.commute(commute_location)

                else:
                    print("\n*Error* Unrecognised option, please enter one of the specified options above.\n")
        else:
            print("\n\n*Error* Unrecognised option, please enter one of the specified options above.\n\n")

    #   End of Function

main()
#call main
