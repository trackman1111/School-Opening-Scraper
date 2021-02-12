from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests
import re
import csv

for school in ["hi"]:
    url = "https://ed.sc.gov/districts-schools/schools/district-and-school-closures/operational-status/"
    page = requests.get(url)

    schoolinfo = {} #(str_name, str_status)
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

    with open("South_Carolina.csv", 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(csv_columns)
        for key, value in schoolinfo.items():
           writer.writerow([key, value])

    print(schoolinfo)
