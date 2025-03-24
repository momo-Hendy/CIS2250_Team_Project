import sys
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
# from matplotlib import ticker as ticktools

'''
how to get certain data out of the csv file to use for the graph

By: tutorialspoint
Title: How is Seaborn used to filter and select specific rows or columns from my data?
https://www.tutorialspoint.com/how-is-seaborn-used-to-filter-and-select-specific-rows-or-columns-from-my-data

By: stackoverflow
Title: Selecting with complex criteria from pandas.DataFrame
To use multiple conditions on the data in the csv file
https://stackoverflow.com/questions/15315452/selecting-with-complex-criteria-from-pandas-dataframe

By: Kimberly Fessel
Title: Matplotlib Secondary y-Axis || Add another y-axis with Matplotlib twinx || Matplotlib Tips
https://www.youtube.com/watch?v=_FO8jUMa65M
In order to get a legend the right way using two different data files.


'''

def question1_Graph(jobVacanciesCSV, commuteTimeCSV, outputGraph):
    geo = 15
    labels = []
    save = ""
    if len(argv) != 4:
        print("*Error* You need this file format create_name_category_plot.py <data file> <pdf file>")
        sys.exit(-1)
    while(geo < 0 or geo > 11):
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
        if(geo > 14):
            print("*Error* this is an unknown value please enter one of the values specified above\n", file = sys.stderr)
    
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
        jobVacancyRegion = "New Bruswick"
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
    
    # jobVacanciesCSV = argv[1]
    # commuteTimeCSV = argv[2]
    # outputGraph = argv[3]

    try:
        jobVacanciesCSV_df = pd.read_csv(jobVacanciesCSV)

    except IOError as err:
        print("Unable to open source file", jobVacanciesCSV,
                ": {}".format(err), file=sys.stderr)
        sys.exit(-1)

    try:
        commuteTimeCSV_df = pd.read_csv(commuteTimeCSV)

    except IOError as err:
        print("Unable to open source file", commuteTimeCSV,
                ": {}".format(err), file=sys.stderr)
        sys.exit(-1)


    fig, ax1 = plt.subplots()
    commuteTimeByRegion = commuteTimeCSV_df.loc[(commuteTimeCSV_df['GEO'] == commuteRegion)]
    line1 = ax1.plot(commuteTimeByRegion['Year'], commuteTimeByRegion['VALUE'], color = 'red', label = f"Commute Time in {jobVacancyRegion}")
    ax1.set_ylabel('Average Commute Time in Minutes')
    ax1.tick_params(axis = 'y')

    jobVacanciesByRegion = jobVacanciesCSV_df.loc[(jobVacanciesCSV_df['GEO'] == jobVacancyRegion) &
        (jobVacanciesCSV_df['REF_DATE'].astype(str).isin(["2021-05", "2022-05", "2023-05", "2024-05"]))]


    # jobVacanciesByRegion = jobVacanciesByRegion.loc['-05' in jobVacanciesByRegion['REF_DATE'] ]
    ax2 = ax1.twinx()
    line2 = ax2.plot(commuteTimeByRegion['Year'], jobVacanciesByRegion['VALUE'], color = 'blue', label = f"Job Vacancies in {jobVacancyRegion}")
    ax2.set_ylabel('Number of Job Vacancies')
    ax2.tick_params(axis = 'y')
    ax2.ticklabel_format(style='plain', axis='y')
    # ax1.xticks(rotation=45)
    
    # This was coppied from a video ##########
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels)
    ax1.set_title('Comparison Between Commute times and Job Vacancies')
    ###########################################
    while (save != "yes" and save != "no"):
        save = input("Would you like to save the graph? (Yes or No): ")
        save = save.lower()
        if (save == "yes"):
            outputName = input("What would you like the file to be called?")
            fig.savefig(outputName)
        elif save == "no":
            plt.show()
        else:
            print("*Error* you did not enter Yes, or No. Please enter one or the other.")
    # concatenated = pd.concat([ax1, ax2])
    # sns.lineplot(x = "Year", y = "VALUE", hue="GEO", data=concatenated)



    # p1, = ax1.plot(x_axis, "Year") 
    # ax1.legend(['Average Commute Time in Minutes'], loc="upper left")
    
    
    # ax2 = ax1.twinx()
    # ax2.legend(['Number of Job Vacancies'], loc="upper right")
    # ax = jobVacanciesCSV_df.plot(figsize=(20,10))

    # commuteTimeCSV_df.plot(ax=ax)






    # commuteTimeCSV_df.close()
    # commuteTimeCSV_df = pd.read_csv(commuteTimeCSV)
    # fig = plt.figure()

    # Canada = commuteTimeCSV_df[commuteTimeCSV_df['GEO'] == 'Canada'].reset_index(drop=False)

    # This creates a lineplot using seaborn.  We simply refer to
    # the various columns of data we want in our pandas data structure.
    # may = jobVacanciesCSV_df['-05' in jobVacanciesCSV_df['REF_DATE'].reset_index(drop=False)]
    # commuteDate = commuteTimeCSV_df[commuteTimeCSV_df['Year'].reset_index(drop=True)]
    # commuteLocation = commuteTimeCSV_df[commuteTimeCSV_df['GEO'] .reset_index(drop=True)]

    # output = sns.barplot(x = "Year", y = "Value", hue="GEO", data=commuteTimeCSV_df)
    # jobVacanciesOutput = sns.barplot(x = "REF_DATE", y = "VALUE", hue="GEO", data=jobVacanciesCSV_df)
    
    # fig, ax1 = plt.subplots()
    # color = 'tab:red'
    # ax1.set_xlabel('Date')

    # plt.plot(output, color=color)
    # plt.gcf().autofmt_xdate()
    # ax1.tick_params(axis='y', labelcolor=color)
    # ax1.set_ylabel('Average Commute Time in Minutes', color=color)

    # ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    # color = 'tab:blue'
    # ax2.set_ylabel('Number of Job Vacancies', color=color)  # we already handled the x-label with ax1
    # ax2.plot(jobVacanciesOutput, color=color)
    # ax2.tick_params(axis='y', labelcolor=color)
    # plt.xticks(rotation=45)

    # plt.title('Bitcoin price vs Bitcoin Tweet Sentiment')
    # fig.tight_layout()  # otherwise the right y-label is slightly clipped
    # plt.show()
    
    
    
    # plt.setp(output.get_legend().get_texts(), fontsize='10')

    # Now we can save the matplotlib figure that seaborn has drawn
    # for us to a file
    # fig.savefig(outputGraph, bbox_inches="tight")
    # for rowDataFeilds in commuteTimeCSV:
    #     if lineNumber > 0:
    #         for i in range (1, 5):
    

        # lineNumber += 1
question1_Graph(sys.argv)