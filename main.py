import requests
import csv
import virginia
import oregon


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mainFile = open('SchoolDistricts.csv', 'w')
    csv_writer = csv.writer(mainFile)
    csv_writer.writerow(["State", "District", "Mode", "Date Updated"])
    mainFile.close()

    #oregon.main()
    #virginia.main()

