#This file is to collect the needed data feilds from each data file
import sys
import csv
def main(argv):
    #Taking in one data file at a time
    if len(argv) != 2:
        print("*Error* Wrong number of expected arguments", file = sys.stderr())
        sys.exit(1)

    #Collecting the data file
    dataFile = "../original_data_files/Reasons_Not_Looking_For_Work"
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


main(sys.argv)
