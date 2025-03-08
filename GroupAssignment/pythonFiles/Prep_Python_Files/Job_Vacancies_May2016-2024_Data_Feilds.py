
#This file is to collect the needed data feilds from each data file
import sys
import csv
def main(argv):
    # canada = "Canada"
    # newfoundland = "Newfoundland and Labrador"
    # pei = "Prince Edward Island"
    # novaScotia = "Nova Scotia"
    # newBrunswick = "New Brunswick"
    # quebec = "Quebec"
    # ontario = "Ontario"
    # manitoba = "Manitoba"
    # saskatchewan = "Saskatchewan"
    # alberta = "Alberta"
    # britishColumbia = "British Columbia"
    # yukon = "Yukon"
    # northwestTerritories = "Northwest Territories"
    # nunavut = "Nunavut"

    #Taking in one data file at a time
    if len(argv) != 3:
        print("*Error* Wrong number of expected arguments", file = sys.stderr())
        sys.exit(1)

    #Collecting the data file
    dataFile = "../original_data_files/Job_Vacancies.csv"
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
        statistics = rowDataFeilds[3]
        UOM = rowDataFeilds[4]
        value = rowDataFeilds[10]

        #Check to see if the month is may
        if ("-05" in REF_DATE):
            if statistics == "Job vacancies":
                if UOM == "Number":
                    print("%s,%s,%s,%s,%s" % (REF_DATE, GEO, statistics, UOM, value))



main(sys.argv)