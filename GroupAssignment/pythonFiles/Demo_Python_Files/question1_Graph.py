import sys
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
# from matplotlib import ticker as ticktools

'''
question1_Graph.py

Author(s):  Wyatt Evans 1293147, Harveen Harveen 1337280, Indigo Asher 1348315

Project: Milestone III
Date of Last Update: March 23rd 2025

Functional Summary
    This function takes in three arguments
    1: the location of the updated jobVacncies csv file
    2: The location of the updated AverageCommuteTime csv file
    3: the location of where the graph will be saved if saved

    This program creates a line graph based off of data collected by statistics canada and it takes in a summerized version of that data
    the graph that is produced is either of canada or one of the provences in canada

    which then they can choose to save the plot or not and if they dont then they can view it

    and it creates 2 lines

    1 for the average commute time and 1 for job vacancies these are across the years 2021-2024
'''

'''
how to get certain data out of the csv file to use for the graph

By: Andrew Hamilton-Wright
Titles: create_name_rank_plot.py, amd create_name_rank_category_plot.py
We learned how to save the plots from here

By: Python Graph Gallery
Title: Dual Y axis with Python and Matplotlib
https://python-graph-gallery.com/line-chart-dual-y-axis-with-matplotlib/
To create a plot with multiple y-axis on it

By: tutorialspoint
Title: How is Seaborn used to filter and select specific rows or columns from my data?
https://www.tutorialspoint.com/how-is-seaborn-used-to-filter-and-select-specific-rows-or-columns-from-my-data
There were some unnessasary data still for this question but is usful for other questions

By: stackoverflow
Title: Selecting with complex criteria from pandas.DataFrame
https://stackoverflow.com/questions/15315452/selecting-with-complex-criteria-from-pandas-dataframe
To use multiple conditions on the data in the csv file

By: Kimberly Fessel
Title: Matplotlib Secondary y-Axis || Add another y-axis with Matplotlib twinx || Matplotlib Tips
https://www.youtube.com/watch?v=_FO8jUMa65M
In order to get a legend the right way using two different data files.

By: tutorialspoint
Title: How to repress scientific notation in factorplot Y-axis in Seaborn / Matplotlib?
https://www.tutorialspoint.com/how-to-repress-scientific-notation-in-factorplot-y-axis-in-seaborn-matplotlib#:~:text=PythonData%20Visualization-,To%20repress%20scientific%20notation%20in%20factorplot%20Y%2Daxis%20in%20Seaborn,plain%22%20in%20ticklabel_format()method.
to change the y-axis from scientific notation to numbers

By: GeeksforGeeks
Title: How to Convert Pandas Columns to String
https://www.geeksforgeeks.org/how-to-convert-pandas-columns-to-string/
had to check values in the csv files where it had to be a string



'''

def question1_Graph(jobVacancies, AverageCommuteTime, OutputLocation):
    geo = 15
    labels = []
    save = ""
    # if len(argv) != 4:
    #     print("*Error* You need this file format create_name_category_plot.py <data file> <data file> <output graph location>")
    #     sys.exit(-1)
    while(geo > 11 or geo == 0):
        try:
            geo = int(input("Please select which area you would like to compare:\n\n"
                        "Canada: 1\n"
                        "Newfoundland and Labrador: 2\n"
                        "Prince Edward Island: 3\n"
                        "Nova Scotia: 4\n"
                        "New Brunswick: 5\n"
                        "Quebec: 6\n"
                        "Ontario: 7\n"
                        "Manitoba: 8\n"
                        "Saskatchewan: 9\n"
                        "Alberta: 10\n"
                        "British Columbia: 11\n"
                        "Enter any Negitive Number to exit: "))
        except ValueError:
            print("\n\n*Error* Please enter only the integer (Whole Number) for each option\n\n", file = sys.stderr)
            sys.exit(1)
        if(geo > 14 or geo == 0):
            print("*Error* this is an unknown value please enter one of the values specified above\n", file = sys.stderr)
        if geo < 0:
            print("")
            sys.exit(0)
    #This section just switches the number the user inputs to the region they would like to compare
    if (geo == 1):
        commuteRegion = "Canada"
        jobVacancyRegion = "Canada"
    elif (geo == 2):
        commuteRegion = "Newfoundland  and Labrador"
        jobVacancyRegion = "Newfoundland and Labrador"
    elif (geo == 3):
        commuteRegion = "Prince  Edward Island"
        jobVacancyRegion = "Prince Edward Island"
    elif (geo == 4):
        commuteRegion = "Nova  Scotia"
        jobVacancyRegion = "Nova Scotia"
    elif (geo == 5):
        commuteRegion = "New  Brunswick"
        jobVacancyRegion = "New Brunswick"
    elif (geo == 6):
        commuteRegion = "Quebec"
        jobVacancyRegion = "Quebec"
    elif (geo == 7):   
        commuteRegion = "Ontario"
        jobVacancyRegion = "Ontario"
    elif (geo == 8):
        commuteRegion = "Manitoba"
        jobVacancyRegion = "Manitoba"
    elif (geo == 9):
        commuteRegion = "Saskatchewan"
        jobVacancyRegion = "Saskatchewan"
    elif (geo == 10):
        commuteRegion = "Alberta"
        jobVacancyRegion = "Alberta"
    elif (geo == 11):
        commuteRegion = "British  Columbia"
        jobVacancyRegion = "British Columbia"

    #End of converting regions

    
    jobVacanciesCSV = jobVacancies
    commuteTimeCSV = AverageCommuteTime
    outputGraph = OutputLocation

    try:
        jobVacanciesCSV_df = pd.read_csv(jobVacanciesCSV)

    except IOError as err:
        print("Unable to open source file", jobVacanciesCSV,
                ": {}".format(err), file=sys.stderr)
        sys.exit(1)

    try:
        commuteTimeCSV_df = pd.read_csv(commuteTimeCSV)

    except IOError as err:
        print("Unable to open source file", commuteTimeCSV,
                ": {}".format(err), file=sys.stderr)
        sys.exit(1)


    fig, ax1 = plt.subplots()
    commuteTimeByRegion = commuteTimeCSV_df.loc[(commuteTimeCSV_df['GEO'] == commuteRegion)]

    line1 = ax1.plot(commuteTimeByRegion['Year'], commuteTimeByRegion['VALUE'], color = 'red', label = f"Commute Time in {jobVacancyRegion}")
    ax1.set_ylabel('Average Commute Time in Minutes')
    

    jobVacanciesByRegion = jobVacanciesCSV_df.loc[(jobVacanciesCSV_df['GEO'] == jobVacancyRegion) &
        (jobVacanciesCSV_df['REF_DATE'].astype(str).isin(["2021-05", "2022-05", "2023-05", "2024-05"]))]

    ax2 = ax1.twinx()
    line2 = ax2.plot(commuteTimeByRegion['Year'], jobVacanciesByRegion['VALUE'], color = 'blue', label = f"Job Vacancies in {jobVacancyRegion}")
    ax2.set_ylabel('Number of Job Vacancies')
    

    #This was taken so the style stays as is and does not become scientific notation
    ax2.ticklabel_format(style='plain', axis='y')

    ####### This was coppied from a video and edited to fit this program ##########
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels)
    ax1.set_title('Comparison Between Commute times and Job Vacancies')
    ###############################################################################
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

# question1_Graph(str, str, str)