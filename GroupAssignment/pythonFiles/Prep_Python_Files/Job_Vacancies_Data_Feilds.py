
#This file is to collect the needed data feilds from each data file
import sys
import csv
def main(argv):
    #Taking in one data file at a time
    if len(argv) != 3:
        print("*Error* Wrong number of expected arguments", file = sys.stderr())
        sys.exit(1)

    #Collecting the data file
    dataFile = argv[1]
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


main(sys.argv)