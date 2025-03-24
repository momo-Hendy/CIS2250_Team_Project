import sys
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import csv
import numpy as np

'''
question3_Graph.py

Author(s):  Wyatt Evans 1293147, Harveen Harveen 1337280, Indigo Asher 1348315

Project: Milestone III
Date of Last Update: March 23th 2025

Functional Summary
    This function takes in three arguments
    1: the location of the updated jobVacncies csv file
    2: The location of the updated ResonforNotWorking csv file
    3: the location of where the graph will be saved if saved

    This program creates a bar graph based off of data collected by statistics canada and it takes in a summerized version of that data
    the graph can be based off of three different reasons:

    1: Total, not in the labour force
    2: Wanted work , reason - illness
    3: Not in the labour force and did not want work or not available

    and it creates 4 bars per the two years that it covers

    3 for the reasons not looking for work and 1 for job vacancies

    '''

'''
By: Andrew Hamilton-Wright
Titles: create_name_rank_plot.py, amd create_name_rank_category_plot.py
We learned how to save the plots from here

By: tutorialspoint
Title: How is Seaborn used to filter and select specific rows or columns from my data?
https://www.tutorialspoint.com/how-is-seaborn-used-to-filter-and-select-specific-rows-or-columns-from-my-data
There were some unnessasary data still for this question but is usful for other questions

By: stackoverflow
Title: Selecting with complex criteria from pandas.DataFrame
https://stackoverflow.com/questions/15315452/selecting-with-complex-criteria-from-pandas-dataframe
To use multiple conditions on the data in the csv file

By: Stack Overflow
Title: Plotting multiple bars with matplotlib using ax.bar()
https://stackoverflow.com/questions/56076590/plotting-multiple-bars-with-matplotlib-using-ax-bar
So we could plot multiple bar graphs

By: Stack Overflow
Title: matplotlib bar plot add legend from categories dataframe column
https://stackoverflow.com/questions/57340415/matplotlib-bar-plot-add-legend-from-categories-dataframe-column
bar graphs have different syntax for the legends then line graphs so we needed another way to do it

By: tutorialspoint
Title: How to repress scientific notation in factorplot Y-axis in Seaborn / Matplotlib?
https://www.tutorialspoint.com/how-to-repress-scientific-notation-in-factorplot-y-axis-in-seaborn-matplotlib#:~:text=PythonData%20Visualization-,To%20repress%20scientific%20notation%20in%20factorplot%20Y%2Daxis%20in%20Seaborn,plain%22%20in%20ticklabel_format()method.
to change the y-axis from scientific notation to numbers

By:
Title: 
https://www.geeksforgeeks.org/how-to-change-axes-limits-in-seaborn/
how to create multiple axis in seaboarn
'''

def question3_Graph(jobVacancies, reasonsNotWorking, OutputLocation):
    rowNumber = 0
    numOfVacancies = 0
    sumOfVacancies = [0,0]
    averageVacancies = [0, 0]
    jobVacanciesCSV = jobVacancies
    notWorkingCSV = reasonsNotWorking
    outputGraph = OutputLocation
    year = ""
    save = ""
    years = ["2017", "2022"]
    reason = ""
    region = "Canada"
    try:
        jobVacanciesCSV_df = pd.read_csv(jobVacanciesCSV)
        jobVacanciesAverage = open(jobVacanciesCSV)

    except IOError as err:
        print("Unable to open source file", jobVacanciesCSV,
                ": {}".format(err), file=sys.stderr)
        sys.exit(1)

    try:
        notWorkingCSV_df = pd.read_csv(notWorkingCSV)

    except IOError as err:
        print("Unable to open source file", notWorkingCSV,
                ": {}".format(err), file=sys.stderr)
        sys.exit(1)
    jobVacancies_reader = csv.reader(jobVacanciesAverage)

    for rowDataFeilds in jobVacancies_reader:
        if rowNumber != 0:
            year = rowDataFeilds[0]
            region = rowDataFeilds[1]
            numOfVacancies = int(rowDataFeilds[4])
            if "2017" in year:
                if region == "Canada":
                        sumOfVacancies[0] += numOfVacancies
            elif "2022" in year:
                if region == "Canada":
                        sumOfVacancies[1] += numOfVacancies

        rowNumber += 1
    for i in range (0, len(sumOfVacancies)):
        averageVacancies[i] = sumOfVacancies[i] / 12

    notWorkingTotal = notWorkingCSV_df.loc[(notWorkingCSV_df['Reasons not looking for work'] == "Total, not in the labour force")]
    notWorkingIllness = notWorkingCSV_df.loc[(notWorkingCSV_df['Reasons not looking for work'] == "Wanted work , reason - illness")]
    notInWorkingFource = notWorkingCSV_df.loc[(notWorkingCSV_df['Reasons not looking for work'] == "Not in the labour force and did not want work or not available")]

    fig, ax1 = plt.subplots()
    bar_width = 0.2
    x = np.arange(len(years))
    ax1.bar(x - bar_width * 1.5, notWorkingTotal['VALUE'], bar_width, color = 'red', label = "Total, not in the labour force")
    ax1.set_ylabel('Number of people not working')
    ax1.bar(x - bar_width/2, notWorkingIllness['VALUE'], bar_width, color = 'green', label = "Wanted work , reason - illness")
    ax1.bar(x + bar_width/2, notInWorkingFource['VALUE'], bar_width, color = 'purple', label = "Job Vacancies in Not in the labour force and did not want work or not available")
    ax1.set_xticks(x)
    ax1.set_xticklabels(years)

    ax4 = ax1.twinx()
    ax4.bar(x + bar_width * 1.5, averageVacancies, bar_width, color = 'blue', label = f"Job Vacancies in {years}")
    ax4.set_ylabel('Number of Job Vacancies')


    #This was taken so the style stays as is and does not become scientific notation
    ax4.ticklabel_format(style='plain', axis='y')
    ax1.ticklabel_format(style='plain', axis='y')
    ####### This was coppied from a stack overflow#################################
    colours = {'Total, not in the labour force':'red', 'Wanted work , reason - illness':'green', 
              'Job Vacancies in Not in the labour force and did not want work or not available': 'purple',
              'Number of Job Vacancies': 'blue'}         
    labels = list(colours.keys())
    handles = [plt.Rectangle((0,0),1,1, color=colours[label]) for label in labels]
    plt.legend(handles, labels)
    ###############################################################################
    ax1.set_title('Comparison Between Reasons why People are not Working and Job Vacancies')
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



# question3_Graph(str, str, str)