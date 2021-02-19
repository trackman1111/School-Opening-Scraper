from _csv import reader

from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests
import re
import csv
import lxml
from datetime import date


def main():

    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQipdjO8QWhilhhJ4bX0FBebnHEzK1G3LEDQbE_S-xRvs2t0oHNm--acHwMRFmL9uKw4cXcOUqy1V66/pubhtml"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')

    table = soup.find_all("table")[0]
    with open("Colorado.csv", "w") as f:
        csv_writer = csv.writer(f)
        index = 0
        for row in table.find_all("tr"):
            if index > 8 and index != 10:
                csv_writer.writerows([[td.text for td in row.find_all("td")]])
            index = index + 1
    copy_to_main()

def copy_to_main():
    f1 = open("Colorado.csv", 'r')
    f2 = open('SchoolDistricts.csv', 'a')
    csv_reader = reader(f1)
    csv_writer = csv.writer(f2)
    isFirst = True;
    for row in csv_reader:
        if isFirst:
            isFirst = False
        else:
            school_status  = "Elementary: " + row[6] + "Middle/High: " + row[7]
            csv_writer.writerow(["Colorado", row[1],school_status, "", "", "", row[8], date.today()])
    f1.close()
    f2.close()
