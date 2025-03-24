'''
demo_Menu.py

Author(s):  Wyatt Evans 1293147, Harveen Harveen 1337280, Indigo Asher 1348315

Project: Milestone III
Date of Last Update: March 23th 2025

Functional Summary
    File implements a menu to the project, allowing for user accesability. 
    Based on user decisions in the menu, call on 1 of 3 graph files and send which datafields they require.
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

    vacancies_location = "" 
    education_location = ""
    commute_location = ""
    disabilites_location = ""
    output_location = "" 

    print("CIS2250-W25-Project Menu")
    while user_choice != -1:
        fileOutput = ""
        print("Option 1: Print Graph From Job Vaccancy Questions")
        print("Option 2: Get Data From Files")
        temp_user_choice = input("Enter 1, 2, or -1 to exit: ")
        try:
            user_choice = int(temp_user_choice)
        except ValueError:
            print("\n\n*Error* Please enter only the integer (Whole Number) for each option i.e. either 1, 2, 3, or -1 to exit\n\n", file = sys.stderr)
            sys.exit(1)

        if user_choice == -1:
            print("\n\nExiting.......\n\n")
            break
        elif user_choice == 1:
            print("\nChoose Question:")
           
            print("Option 1: Do job vacancies affect the average commute time across the provinces?")
            print("Option 2: Do regions with lower education levels have differing job vacancy rates compared to regions with higher education rates?")
            print("Option 3: What is the correlation between people with disabilities who are unable to find work and the amount of job vacancies?")
                
            temp_user_choice2 = input("Enter 1, 2, or 3: ")
            try:
                user_choice2 = int(temp_user_choice2)
            except ValueError:
                print("\n\n*Error* Please enter only the integer (Whole Number) for each option i.e. either 1, 2, 3, or -1 to exit\n\n", file = sys.stderr)
                sys.exit(1)

            if user_choice2 == 1:
                if vacancies_location == "" and commute_location == "":
                    print("\n*Error* Pre-processing for csv files has not been completed. \nplease complete Option 2: Get Data From Files first\n")
                else:
                    output_location = "../../Output_Graphs/Question1/" 

                    question1_Graph.question1_Graph(vacancies_location, commute_location, output_location)

            elif user_choice2 == 2:
                if vacancies_location == "" and education_location == "":
                    print("\n*Error* Pre-processing for csv files has not been completed. \nplease complete Option 2: Get Data From Files first\n")
                else:
                    output_location = "../../Output_Graphs/Question2/" 
                    question2_Graph.question2_Graph(vacancies_location, education_location, output_location)

            elif user_choice2 == 3:
                if vacancies_location == "" and disabilites_location == "":
                    print("\n*Error* Pre-processing for csv files has not been completed. \nplease complete Option 2: Get Data From Files first\n")
                else:
                    output_location = "../../Output_Graphs/Question3/" 
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
                    while(not vacancies_location.endswith(".csv")):
                        vacancies_location = input("Please enter the file name you would like to print in: ")
                        if(not vacancies_location.endswith(".csv")):
                            print("*Error* You did not enter a csv file")
                    vacancies_location = path + "/../../data_fields_from_data_files/" + vacancies_location
                    jobVacancies(vacancies_location)

                elif user_choice3 == 2:
                    while(not education_location.endswith(".csv")):
                        education_location = input("Please enter the file name you would like to print in: ")
                        if(not education_location.endswith(".csv")):
                            print("*Error* You did not enter a csv file")
                    education_location = path + "/../../data_fields_from_data_files/" + education_location
                    education(education_location)

                elif user_choice3 == 3:
                    while(not disabilites_location.endswith(".csv")):
                        disabilites_location = input("Please enter the file name you would like to print in: ")
                        if(not disabilites_location.endswith(".csv")):
                            print("*Error* You did not enter a csv file")
                    disabilites_location = path + "/../../data_fields_from_data_files/" + disabilites_location
                    disabilites(disabilites_location)
                
                elif user_choice3 == 4:
                    while(not commute_location.endswith(".csv")):
                        commute_location = input("Please enter the file name you would like to print in: ")
                        if(not commute_location.endswith(".csv")):
                            print("*Error* You did not enter a csv file")
                    commute_location = path + "/../../data_fields_from_data_files/" + commute_location
                    commute(commute_location)

                else:
                    print("\n*Error* Unrecognised option, please enter one of the specified options above.\n")
        else:
            print("\n\n*Error* Unrecognised option, please enter one of the specified options above.\n\n")

    #   End of Function

main()
#call main
