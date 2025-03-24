import sys
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import csv
import numpy as np

def question3_Graph(jobVacanciesCSV, notWorkingCSV, outputGraph):
    rowNumber = 0
    numOfVacancies = 0
    sumOfVacancies = [0,0]
    averageVacancies = [0, 0]
    # jobVacanciesCSV = argv[1]
    # notWorkingCSV = argv[2]
    # outputGraph = argv[3]
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
    bar1 = ax1.bar(x - bar_width * 1.5, notWorkingTotal['VALUE'], bar_width, color = 'red', label = "Total, not in the labour force")
    ax1.set_ylabel('Number of people not working')
    bar2 = ax1.bar(x - bar_width/2, notWorkingIllness['VALUE'], bar_width, color = 'green', label = "Wanted work , reason - illness")
    bar3 = ax1.bar(x + bar_width/2, notInWorkingFource['VALUE'], bar_width, color = 'purple', label = "Job Vacancies in Not in the labour force and did not want work or not available")
    ax1.set_xticks(x)
    ax1.set_xticklabels(years)

    ax4 = ax1.twinx()
    bar4 = ax4.bar(x + bar_width * 1.5, averageVacancies, bar_width, color = 'blue', label = f"Job Vacancies in {years}")
    ax4.set_ylabel('Number of Job Vacancies')


    #This was taken so the style stays as is and does not become scientific notation
    ax4.ticklabel_format(style='plain', axis='y')
    ax1.ticklabel_format(style='plain', axis='y')
    ####### This was coppied from a video and edited to fit this program ##########
    colours = {'Total, not in the labour force':'red', 'Wanted work , reason - illness':'green', 
              'Job Vacancies in Not in the labour force and did not want work or not available': 'purple',
              'Number of Job Vacancies': 'blue'}         
    labels = list(colours.keys())
    handles = [plt.Rectangle((0,0),1,1, color=colours[label]) for label in labels]
    plt.legend(handles, labels)
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
            plt.show()
        else:
            print("*Error* you did not enter Yes, or No. Please enter one or the other.")



question3_Graph(sys.argv)