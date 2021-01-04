import csv
import model

def writeToCSV(Person, csvpath):
    with open (csvpath, mode='w') as pfile:
        pwriter = csv.writer(pfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        rowdata = [Person.fname, Person.lname, Person.phone, Person.adress]
        pwriter.writerow(rowdata)