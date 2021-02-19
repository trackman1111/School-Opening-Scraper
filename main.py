import requests
import csv
import alabama
import south_carolina
import tennessee


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mainFile = open('SchoolDistricts.csv', 'w')
    csv_writer = csv.writer(mainFile)
    csv_writer.writerow(["State", "District", "Mode", "Address", "Latitude", "Longitude", "Date Updated"])
    mainFile.close()
    alabama.main()
    south_carolina.main()
    tennessee.main()


