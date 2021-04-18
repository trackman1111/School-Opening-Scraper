from _csv import reader
from bs4 import BeautifulSoup
import requests
import re
import csv
from datetime import date, datetime


def main():
    for school in ["hi"]:
        url = "https://ed.sc.gov/districts-schools/schools/district-and-school-closures/operational-status/"
        page = requests.get(url)

        schoolinfo = {}  # (str_name, str_status)
        if page.status_code == 200:
            soup = BeautifulSoup(page.text, 'lxml')

            for schoolpanel in soup.find_all(class_="panel panel-default"):
                schname = schoolpanel.find(class_="panel-title").contents[0].strip()
                schltbl = schoolpanel.find_all(class_="table districtInfo")[0]
                schpol = schltbl.find(class_=re.compile("bg.*")).contents[0]

                schoolinfo[schname] = schpol

        else:
            print("page request error with ", page.status_code)

        csv_columns = ['SchoolDistrict', 'Policy']

        with open("out/South_Carolina" + datetime.now().strftime('%m-%d-%Y') + ".csv", 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(csv_columns)
            for key, value in schoolinfo.items():
                writer.writerow([key, value])


def copy_to_main():
    f1 = open("South_Carolina.csv", 'r')
    f2 = open('SchoolDistricts.csv', 'a')
    csv_reader = reader(f1)
    csv_writer = csv.writer(f2)
    is_first = True;
    for row in csv_reader:
        if is_first:
            is_first = False
        else:
            csv_writer.writerow(["South Carolina", row[0], row[1], "", "", "", "", date.today()])
    f1.close()
    f2.close()


#main()
