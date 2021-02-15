import requests
import urllib
import csv
from openpyxl import load_workbook
from bs4 import BeautifulSoup


def main():
    download_xslx()
    copy_to_new_csv()


def download_xslx():
    # Get html of page
    url = "https://www.oregon.gov/ode/students-and-family/healthsafety/Pages/2020-21-School-Status.aspx"
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Get the most recent update link
    path = soup.body.main.div.contents[9].li.a['href']
    dataUrl = "https://www.oregon.gov/" + path

    # Retrieve cvs file
    urllib.request.urlretrieve(dataUrl, './OregonOriginal.xlsx')
    print("Downloaded OR xlsx")


def copy_to_new_csv():
    dest = open('Oregon.csv', 'w', newline='')
    csv_writer = csv.writer(dest)
    csv_writer.writerow(["State", "District", "Mode", "Date Updated"])
    wb = load_workbook('OregonOriginal.xlsx')
    districtSheet = wb['District List']
    prevDistrict = ""
    i = 0
    for row in districtSheet.iter_rows(values_only=True):
        if i == 0:
            i += 1
            continue
        curDistrict = row[2]
        if curDistrict is None:
            break
        if curDistrict == prevDistrict:
            # Repeat district, skip
            continue
        reportWeek = row[3]
        mode = row[5]
        dateUpdated = reportWeek[11:]  # End date of report week

        csv_writer.writerow(["Oregon", curDistrict, mode, dateUpdated])
        i += 1


main()
