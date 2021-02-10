# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import csv
import virginia


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mainFile = open('SchoolDistricts.csv', 'w')
    csv_writer = csv.writer(mainFile)
    csv_writer.writerow(["State", "District", "Mode", "Date Updated"])
    mainFile.close()
    virginia.main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
