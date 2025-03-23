'''
demo_Menu.py

Author(s):  Wyatt Evans 1293147, Harveen Harveen 1337280, Indigo Asher 1348315

Project: Milestone III
Date of Last Update: March 23th 2025

Functional Summary
    File implements a menu to the project, allowing for user accesability. 
    Based on user decisions in the menu, call on 1 of 3 graph files and send which datafields they require.
'''

# import tkinter as tk
# from tkinter import messagebox

from tkinter import *
import sys
from pathlib import Path

from question1_Graph import *
#from question2_Graph import *
#from question3_Graph import *
from demo_Files import *

#will add proper gui once have basic functionality
# win = Tk()
# win.title("CIS2250-W25-Project Menu")

# menu = Menu(win)
# win.config(menu=menu)

# data = Menu(menu)
# menu.add_cascade(label="Data", menu=data)

def main():
    user_choice = 0
    path = str(Path.cwd())
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
            print("\nChoose Question:\n")
           
            print("Option 1: Do job vacancies affect the average commute time across the provinces?")
            print("Option 2: Do regions with lower education levels have differing job vacancy rates compared to regions with higher education rates?")
            print("Option 3: What is the correlation between people with disabilities who are unable to find work and the amount of job vacancies?")
                
            temp_user_choice2 = input("Enter 1, 2, or 3: ")
            try:
                user_choice2 = int(temp_user_choice2)
            except ValueError:
                print("\n\n*Error* Please enter only the integer (Whole Number) for each option i.e. either 1, 2, 3, or -1 to exit\n\n", file = sys.stderr)
                sys.exit(1)

            if user_choice2 == -1:
                print("\n\nExiting.......\n\n")
                break
            elif user_choice2 == 1:
                jobVacancies()
                commute()

            elif user_choice2 == 2:
                jobVacancies()
                education()

            elif user_choice2 == 3:
                jobVacancies()
                disabilites()

            else:
                print("\n\n*Error* Unrecognised option, please enter one of the specified options above.\n\n")


        elif user_choice == 2:
            print()
        else:
            print("\n\n*Error* Unrecognised option, please enter one of the specified options above.\n\n")

    #   End of Function

main()
#call main