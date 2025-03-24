import sys
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import csv
import numpy as np

def question2_Graph(jobVacancies, educationLevels, outputLocation):
    lineNumber = 0
    rowNumber = 0
    whatGraph = 0
    educationLevel = 0
    jobVacanciesCSV = jobVacancies
    educationLevelCSV = educationLevels
    outputGraph = outputLocation
    sumOfPeople = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    sumOfVacancies = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    averageVacancies = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    save = ""
    regions = ["Newfoundland and Labrador","Prince Edward Island","Nova Scotia","New Brunswick","Quebec","Ontario","Manitoba","Saskatchewan","Alberta","British Columbia"]
    # if len(argv) != 4:
    #     print("*Error* You need this file format create_name_category_plot.py <data file> <data file> <output graph location>")
    #     sys.exit(-1)

    try:
        jobVacanciesCSV_df = pd.read_csv(jobVacanciesCSV)
        jobVacanciesAverage = open(jobVacanciesCSV)
    except IOError as err:
        print("Unable to open source file", jobVacanciesCSV,
                ": {}".format(err), file=sys.stderr)
        sys.exit(1)

    try:
        sumOfEducation = open(educationLevelCSV)
        educationLevelCSV_df = pd.read_csv(educationLevelCSV)

    except IOError as err:
        print("Unable to open source file", educationLevelCSV,
                ": {}".format(err), file=sys.stderr)
        sys.exit(1)
    while(whatGraph == 0):
        print("Including and onward: Enter a positive number")
        try:
            whatGraph = int(input("up to and includeing: Enter a negitive number:\n"))
        except ValueError:
            print("\n\n*Error* Please enter only the integer (Whole Number) for each option i.e. either 1, 2, 3, or -1 to exit\n\n", file = sys.stderr)
            sys.exit(1)
        if whatGraph == 0:
            print ("*Error* please input a positive or nagitive number", file = sys.stderr)
    while educationLevel > 15 or educationLevel == 0:
        try:   
            educationLevel = int(input("which education Level you would like to see:\n"
                                "No certificate, diploma or degree: 1\n"
                                "High (secondary) school diploma or equivalency certificate: 2\n"
                                "Postsecondary certificate, diploma or degree: 3\n"
                                "Postsecondary certificate or diploma below bachelor level: 4\n"
                                "Apprenticeship or trades certificate or diploma: 5\n"
                                "Non-apprenticeship trades certificate or diploma: 6\n"
                                "Apprenticeship certificate: 7\n"
                                "College, CEGEP or other non-university certificate or diploma: 8\n"
                                "University certificate or diploma below bachelor level: 9\n"
                                "Bachelor’s degree or higher: 10\n"
                                "Bachelor's degree: 11\n"
                                "University certificate or diploma above bachelor level: 12\n"
                                "Degree in medicine, dentistry, veterinary medicine or optometry: 13\n"
                                "Master's degree: 14\n"
                                "Earned doctorate: 15\n"
                                "To Exit Enter a Negitive number\n\n"))
        except ValueError:
            print("\n\n*Error* Please enter only the integer (Whole Number) for each option i.e. 1, 2, 3, ..., 15.\n\n", file = sys.stderr)
            sys.exit(1)
        if(educationLevel > 15 or educationLevel == 0):
            print ("*Error please enter one of the values stated above")
    
    if(educationLevel < 0):
        print("\n\nGoodbye......\n\n")
        sys.exit(0)
    sumOfEducation_reader = csv.reader(sumOfEducation)
    jobVacancies_reader = csv.reader(jobVacanciesAverage)

    for rowDataFeilds in jobVacancies_reader:
        if rowNumber != 0:
            year = rowDataFeilds[0]
            region = rowDataFeilds[1]
            try:
                numOfVacancies = int(rowDataFeilds[4])
            except ValueError:
                print("*Error* the file does not have a value in a cell in the column called VALUE", file=sys.stderr)

            if rowNumber == 0:
                rowNumber + 1
            elif lineNumber > 12:
                lineNumber = 1
            if "2021" in year:

                if (rowNumber >= (educationLevel) and (educationLevel > 0)) or rowNumber <= (educationLevel) and (educationLevel < 0):
                    if region == "Newfoundland and Labrador":
                        if(lineNumber != 0):
                            sumOfVacancies[0] += numOfVacancies
                        lineNumber += 1
                    elif region == "Prince Edward Island":
                        if(lineNumber != 0):
                            sumOfVacancies[1] += numOfVacancies
                        lineNumber += 1
                    elif region == "Nova Scotia":
                        if(lineNumber != 0):
                            sumOfVacancies[2] += numOfVacancies
                        lineNumber += 1
                    elif region == "New Brunswick":
                        if(lineNumber != 0):
                            sumOfVacancies[3] += numOfVacancies
                        lineNumber += 1
                    elif region == "Quebec":
                        if(lineNumber != 0):
                            sumOfVacancies[4] += numOfVacancies
                        lineNumber += 1
                    elif region == "Ontario":
                        if(lineNumber != 0):
                            sumOfVacancies[5] += numOfVacancies
                        lineNumber += 1
                    elif region == "Manitoba":
                        if(lineNumber != 0):
                            sumOfVacancies[6] += numOfVacancies
                        lineNumber += 1
                    elif region == "Saskatchewan":
                        if(lineNumber != 0):
                            sumOfVacancies[7] += numOfVacancies
                        lineNumber += 1
                    elif region == "Alberta":
                        if(lineNumber != 0):
                            sumOfVacancies[8] += numOfVacancies
                        lineNumber += 1
                    elif region == "British Columbia":
                        if(lineNumber != 0):
                            sumOfVacancies[9] += numOfVacancies
                        lineNumber += 1
        rowNumber += 1
    rowNumber = 0
    lineNumber = 0
    for i in range (0, len(sumOfVacancies)):
        averageVacancies[i] = sumOfVacancies[i] / 12
    
    for rowDataFeilds in sumOfEducation_reader:
        if rowNumber == 0:
            rowNumber += 1
            lineNumber = -1

        elif lineNumber > 15:
            lineNumber = 0

        elif(lineNumber < educationLevel and whatGraph > 0):
            lineNumber = lineNumber

        elif(lineNumber > educationLevel and whatGraph < 0):
            lineNumber = lineNumber
        elif ((lineNumber == educationLevel or ((lineNumber > educationLevel) and whatGraph > 0) or ((lineNumber < educationLevel) and whatGraph < 0)) and rowNumber != 0):
            region = rowDataFeilds[0]
            try:
                numOfPeople = int(rowDataFeilds[2])
            except ValueError:
                print("*Error the file does not have a value in a cell in the column called VALUE", file=sys.stderr)
            
            if region == "Newfoundland and Labrador":
                sumOfPeople[0] += numOfPeople

            elif region == "Prince Edward Island":
                sumOfPeople[1] += numOfPeople

            elif region == "Nova Scotia":
                sumOfPeople[2] += numOfPeople

            elif region == "New Brunswick":
                sumOfPeople[3] += numOfPeople

            elif region == "Quebec":
                sumOfPeople[4] += numOfPeople

            elif region == "Ontario":
                sumOfPeople[5] += numOfPeople

            elif region == "Manitoba":
                sumOfPeople[6] += numOfPeople

            elif region == "Saskatchewan":
                sumOfPeople[7] += numOfPeople

            elif region == "Alberta":
                sumOfPeople[8] += numOfPeople

            elif region == "British Columbia":
                sumOfPeople[9] += numOfPeople


        lineNumber += 1
    fig, ax1 = plt.subplots()
    bar_width = 0.4
    x = np.arange(len(regions))
    bar1 = ax1.bar(x - bar_width/2, sumOfPeople, bar_width, color = 'red', label = f"Education Level in {region}")
    ax1.set_ylabel('Number of People with at least a Bachelor\'s Degree')

    ax1.set_xticks(x)
    ax1.set_xticklabels(regions)
    ax1.tick_params(axis='x', labelrotation = 10)

    ax2 = ax1.twinx()
    bar2 = ax2.bar(x + bar_width/2, averageVacancies, bar_width, color = 'blue', label = f"Job Vacancies in {region}")
    ax2.set_ylabel('Number of Job Vacancies')


    #This was taken so the style stays as is and does not become scientific notation
    ax2.ticklabel_format(style='plain', axis='y')
    ax1.ticklabel_format(style='plain', axis='y')
    ####### This was coppied from a video and edited to fit this program ##########
    colours = {'Education Level':'red','Number of Job Vacancies': 'blue'}         
    labels = list(colours.keys())
    handles = [plt.Rectangle((0,0),1,1, color=colours[label]) for label in labels]
    plt.legend(handles, labels)
    ###############################################################################
    ax1.set_title('Comparison Between Education Levels and Job Vacancies')
    while (save != "yes" and save != "no"):
        save = input("Would you like to save the graph? (Yes or No): ")
        save = save.lower()
        if (save == "yes"):
            outputName = input("What would you like the file to be called?")
            # if(outputName.endswith()):
            #     print("*Error* please do not input a ( . ) in the name you just need to specify the name")
            outputName = outputGraph + outputName + ".png"
            fig.savefig(outputName)
        elif save == "no":
            save = input("would you like to view the graph? (Yes or No): ")
            save = save.lower()
            if save == "yes":
                print ("Please Close the graph before continuing")

                plt.show()
            else:
                print("Have a Nice Day!")
                sys.exit(0)
            
        else:
            print("*Error* you did not enter Yes, or No. Please enter one or the other.")

# question2_Graph(str, str, str)